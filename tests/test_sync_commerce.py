import datetime as dt
import json
import os
import unittest
from unittest.mock import patch
from scripts import sync_commerce as s
from scripts import marketing_baseline as m

def api_report(period):
    k = {name:2 for name in m.COUNTS+m.MONEY}
    k.update({name:30 for name in m.RATES})
    return {"status":True,"data":{
        "reportType":"marketing_analytics","timezone":"Asia/Riyadh",
        "currency":"SAR","moneyUnit":"halala","range":period,
        "filters":{"promoCode":"","fulfillmentMethod":"all","paymentProvider":"all",
                   "daysCount":None,"grams":None,"mealsPerDay":None},
        "kpis":k,
        "promoPerformance":[{"code":"KSA96","paidCount":2,"revenueHalala":100,
                             "privateUserId":"DO_NOT_COPY"}],
        "planPerformance":[],"sourceChannels":[],"fulfillmentPerformance":[],
        "paymentProviders":[],"daily":[],"sensitiveRecords":[{"name":"DO_NOT_COPY"}]
    }}

class CommerceSyncTests(unittest.TestCase):
    def test_restricted_identity(self):
        with patch.dict(os.environ,{"ACTIONS_ID_TOKEN_REQUEST_URL":"https://actions.example/token",
                                    "ACTIONS_ID_TOKEN_REQUEST_TOKEN":"temporary"},clear=True):
            with patch.object(s,"request_json",return_value={"value":"aaa.bbb.ccc"}) as mock:
                self.assertEqual(s.get_oidc_identity(),"aaa.bbb.ccc")
                self.assertIn("audience=basicdiet-marketing-analytics-v1",mock.call_args.args[0])
        with patch.dict(os.environ,{},clear=True):
            with self.assertRaisesRegex(RuntimeError,"OIDC"):
                s.get_oidc_identity()

    def test_private_breakdown_allowlist(self):
        report=api_report(m.report_dates("2026-10-07")[30])["data"]
        private=s.safe_breakdown(report)
        self.assertEqual(private["promoPerformance"],[{"code":"KSA96","paidCount":2,"revenueHalala":100}])
        self.assertNotIn("DO_NOT_COPY",json.dumps(private))

    def test_collect_validated_three_windows(self):
        periods=m.report_dates("2026-10-07")
        def fake_request(url,**kwargs):
            d=dict(__import__("urllib").parse.parse_qsl(__import__("urllib").parse.urlsplit(url).query))
            for days,period in periods.items():
                if d.get("from")==period["from"] and d.get("to")==period["to"]:
                    return api_report(period)
            raise AssertionError("Unmatched period")
        with patch.object(s,"request_json",side_effect=fake_request):
            reports=s.collect("signed-short-lived",end_day="2026-10-07",now="2026-10-08T00:00:00Z")
        self.assertEqual([n for n,_ in reports],[30,60,90])
        self.assertEqual(reports[0][1]["kpis"]["firstTimeSubscribers"],2)
        self.assertNotIn("DO_NOT_COPY",json.dumps(reports))

    def test_forged_payload_cannot_be_imported(self):
        def bad(url,**kwargs):
            obj=api_report(m.report_dates("2026-10-07")[30])
            obj["data"]["currency"]="USD"
            return obj
        with patch.object(s,"request_json",side_effect=bad):
            with self.assertRaisesRegex(ValueError,"currency"):
                s.collect("token",end_day="2026-10-07",now="now")

    def test_commit_rejects_wrong_repository(self):
        with patch.dict(os.environ,{"GITHUB_REPOSITORY":"attacker/fork","GITHUB_REF":"refs/heads/main"},clear=True):
            with self.assertRaisesRegex(RuntimeError,"canonical"):
                s.commit_reports([],end_day="2026-10-07",api_key="token")

    def test_commit_never_overwrites(self):
        p=m.report_dates("2026-10-07")[30]
        docs=[(30,{"period":p})]
        with patch.dict(os.environ,{"GITHUB_REPOSITORY":s.OWNER_REPO,"GITHUB_REF":"refs/heads/main"},clear=True):
            calls=[]
            def f(url,**kwargs):
                calls.append(url)
                if url.endswith("/git/ref/heads/main"):return {"object":{"sha":"123"}}
                if url.endswith("/git/commits/123"):return {"tree":{"sha":"tree"}}
                if "/git/trees/tree" in url:return {"tree":[{"path":"data/reports/commerce/2026-10-07/30d.json","type":"blob"}]}
                raise AssertionError("Should not create a blob")
            with patch.object(s,"request_json",side_effect=f):
                with self.assertRaisesRegex(RuntimeError,"overwrite"):
                    s.commit_reports(docs,end_day="2026-10-07",api_key="token")

    def test_commit_batches_all_three(self):
        docs=[(days,{"period":{"days":days}}) for days in s.report_dates("2026-10-07")]
        with patch.dict(os.environ,{"GITHUB_REPOSITORY":s.OWNER_REPO,"GITHUB_REF":"refs/heads/main"},clear=True):
            sent=[]
            def f(url,**kw):
                sent.append((url,kw.get("method","GET"),kw.get("data")))
                if url.endswith("/git/ref/heads/main"):return {"object":{"sha":"head"}}
                if url.endswith("/git/commits/head"):return {"tree":{"sha":"root"}}
                if url.endswith("/git/trees/root?recursive=1"):return {"tree":[]}
                if url.endswith("/git/blobs"):return {"sha":"blob"}
                if url.endswith("/git/trees"):return {"sha":"newtree"}
                if url.endswith("/git/commits"):return {"sha":"newcommit"}
                if url.endswith("/git/refs/heads/main"):return {}
                raise AssertionError(url)
            with patch.object(s,"request_json",side_effect=f):
                paths=s.commit_reports(docs,end_day="2026-10-07",api_key="token")
        self.assertEqual(len(paths),3)
        self.assertEqual(len([x for x in sent if x[1]=="POST" and x[0].endswith("/git/blobs")]),3)
        self.assertEqual(len([x for x in sent if x[1]=="PATCH"]),1)

if __name__=="__main__":
    unittest.main()
