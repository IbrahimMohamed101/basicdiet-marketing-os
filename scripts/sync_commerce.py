#!/usr/bin/env python3
"""Private marketing OS sync: GitHub OIDC -> read-only backend aggregates -> git snapshot."""
from __future__ import annotations
import base64
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

from scripts.marketing_baseline import normalize_report, report_dates

OWNER_REPO = "IbrahimMohamed101/basicdiet-marketing-os"
AUDIENCE = "basicdiet-marketing-analytics-v1"
BACKEND = "https://basicdiet145-production-51e9.up.railway.app/api/marketing-agent/commercial-report"
GITHUB_API = "https://api.github.com/repos/" + OWNER_REPO
MAX_BYTES = 2_000_000
FIELDS = {
    "promoPerformance": ["code","attempts","consumed","reserved","cancelled","paidCount","discountHalala","revenueHalala","conversionRate"],
    "planPerformance": ["daysCount","grams","mealsPerDay","paidTransactions","customersCount","revenueHalala","discountHalala"],
    "sourceChannels": ["key","count","customersCount","amountHalala"],
    "fulfillmentPerformance": ["key","paidTransactions","customersCount","revenueHalala"],
    "paymentProviders": ["key","paidTransactions","customersCount","revenueHalala"],
    "daily": ["date","registrations","checkouts","paidTransactions","revenueHalala"],
}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise RuntimeError("Redirect rejected")

def request_json(url, *, bearer, method="GET", data=None, max_size=MAX_BYTES):
    if not url.startswith("https://"):
        raise RuntimeError("HTTPS required")
    headers = {"Authorization": "Bearer " + bearer, "Accept": "application/json",
               "User-Agent": "BasicDietMarketingOS/1.0"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=(json.dumps(data).encode("utf-8") if data is not None else None),
                                 headers=headers, method=method)
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=30) as response:
        raw = response.read(max_size+1)
        if len(raw)>max_size:
            raise RuntimeError("Response too large")
        obj = json.loads(raw)
        if not isinstance(obj,dict):
            raise RuntimeError("Invalid JSON response")
        return obj

def get_oidc_identity():
    url = os.getenv("ACTIONS_ID_TOKEN_REQUEST_URL","")
    key = os.getenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN","")
    if not url.startswith("https://") or not key:
        raise RuntimeError("GitHub Actions OIDC is not available")
    if len(key)>16000:
        raise RuntimeError("Invalid workflow identity")
    separator = "&" if "?" in url else "?"
    obj = request_json(url + separator + urllib.parse.urlencode({"audience":AUDIENCE}),bearer=key)
    token = obj.get("value")
    if not isinstance(token,str) or len(token)>12000 or token.count(".")!=2:
        raise RuntimeError("GitHub OIDC did not return a JWT")
    return token

def safe_breakdown(data):
    result={}
    for name,keys in FIELDS.items():
        value=data.get(name,[])
        if not isinstance(value,list) or len(value)>100:
            raise RuntimeError("Invalid aggregate breakdown shape")
        entries=[]
        for row in value:
            if not isinstance(row,dict):
                raise RuntimeError("Invalid breakdown row")
            entries.append({k:row[k] for k in keys if k in row})
        result[name]=entries
    return result

def collect(token, *, end_day, now):
    reports=[]
    for days,period in report_dates(end_day).items():
        url = BACKEND + "?" + urllib.parse.urlencode({"from":period["from"],"to":period["to"]})
        wrapper=request_json(url,bearer=token)
        if wrapper.get("status") is not True or not isinstance(wrapper.get("data"),dict):
            raise RuntimeError("Backend returned no aggregate report")
        normalized=normalize_report(wrapper,period,now,"live")
        normalized["origin"]="signed_github_actions_oidc_readonly"
        normalized["breakdowns"]=safe_breakdown(wrapper["data"])
        reports.append((days,normalized))
    return reports

def commit_reports(reports, *, end_day, api_key):
    # Commit all reports atomically, fail closed on existing paths or concurrent main branch update.
    if os.getenv("GITHUB_REPOSITORY") != OWNER_REPO or os.getenv("GITHUB_REF") != "refs/heads/main":
        raise RuntimeError("Sync may only commit from canonical repository main")
    head=request_json(GITHUB_API + "/git/ref/heads/main",bearer=api_key)
    parent=head["object"]["sha"]
    parent_tree=request_json(GITHUB_API+"/git/commits/"+parent,bearer=api_key)["tree"]["sha"]
    previous=request_json(GITHUB_API+"/git/trees/"+parent_tree+"?recursive=1",bearer=api_key)
    known={row["path"] for row in previous["tree"] if row.get("type")=="blob"}
    paths=["data/reports/commerce/"+end_day+"/"+str(days)+"d.json" for days,_ in reports]
    if any(p in known for p in paths):
        raise RuntimeError("One or more snapshots already exist; refusing overwrite")
    nodes=[]
    for (days,payload),path in zip(reports,paths):
        content=json.dumps(payload,ensure_ascii=False,indent=2)+"\n"
        blob=request_json(GITHUB_API+"/git/blobs",bearer=api_key,method="POST",
                          data={"content":content,"encoding":"utf-8"})
        nodes.append({"path":path,"mode":"100644","type":"blob","sha":blob["sha"]})
    tree=request_json(GITHUB_API+"/git/trees",bearer=api_key,method="POST",
                      data={"base_tree":parent_tree,"tree":nodes})
    commit=request_json(GITHUB_API+"/git/commits",bearer=api_key,method="POST",
                        data={"message":"data(marketing): sanitized commercial reports "+end_day,
                              "tree":tree["sha"],"parents":[parent]})
    request_json(GITHUB_API+"/git/refs/heads/main",bearer=api_key,method="PATCH",
                 data={"sha":commit["sha"],"force":False})
    return [p for p in paths]

def main():
    if os.getenv("GITHUB_REPOSITORY")!=OWNER_REPO or os.getenv("GITHUB_REF")!="refs/heads/main":
        raise RuntimeError("Run only in canonical Marketing OS main")
    end_day=(dt.datetime.now(ZoneInfo("Asia/Riyadh")).date()-dt.timedelta(days=1)).isoformat()
    now=dt.datetime.now(dt.timezone.utc).isoformat()
    identity=get_oidc_identity()
    reports=collect(identity,end_day=end_day,now=now)
    gh_token=os.getenv("GITHUB_TOKEN","")
    if not gh_token:
        raise RuntimeError("GitHub contents permission missing")
    files=commit_reports(reports,end_day=end_day,api_key=gh_token)
    print("Synced "+str(len(files))+" aggregate-only commercial snapshots for "+end_day)
    return 0

if __name__=="__main__":
    try:
        sys.exit(main())
    except (ValueError,RuntimeError,KeyError,urllib.error.HTTPError,urllib.error.URLError,OSError) as exc:
        # Never print upstream HTTP response or tokens.
        print("SYNC_FAILED: "+type(exc).__name__,file=sys.stderr)
        sys.exit(2)
