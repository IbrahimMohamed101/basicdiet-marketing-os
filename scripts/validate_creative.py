#!/usr/bin/env python3
"""Validate Drive source evidence and tracked production creative frontmatter.

This is a strict semantic validator (not an attempt to prove genuine owner consent).
Uses PyYAML from requirements-dev.txt and public JSON Schema reference in schemas/.
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import re
import sys

import yaml

ROOT=Path(__file__).resolve().parents[1]
ANGLES={"food_desire","convenience","choice","trust","education","offer","community","behind_scenes"}
STATUSES=("CONCEPT_DRAFT","NEEDS_ASSET_VISUAL_REVIEW","READY_FOR_HUMAN_APPROVAL","APPROVED_BY_OWNER","PRODUCED","PUBLISHED_VERIFIED")
PLATFORMS={"instagram":"instagram.com","facebook":"facebook.com","tiktok":"tiktok.com","snapchat":"snapchat.com"}
REQUIRED={"schema_version","record_id","date","status","platform","format","concepts","selected_angle","selection_reason","asset_ids","primary_kpi","approvals","generated_asset_url","publication"}

def iso(value):
    if not isinstance(value,str):
        raise ValueError("date must be string")
    try:
        d=dt.date.fromisoformat(value)
    except ValueError:
        raise ValueError("invalid YYYY-MM-DD date") from None
    if d.isoformat()!=value or d>dt.datetime.now(dt.timezone.utc).date():
        raise ValueError("invalid or future date")
    return d

def nonempty(value,minimum=2):
    return isinstance(value,str) and len(value.strip())>=minimum

def approve(flag, obj, prefix):
    if type(flag) is not bool:
        raise ValueError(prefix+" must be boolean")
    if flag:
        for k in (prefix+"_by",prefix+"_on",prefix+"_evidence"):
            if not nonempty(obj.get(k),5):
                raise ValueError(prefix+" must have "+k)
        iso(obj[prefix+"_on"])

def validate_assets(index):
    if type(index)!=dict or index.get("schema_version")!=1:
        raise ValueError("invalid Drive source index")
    iso(index.get("checked_at"))
    if not nonempty(index.get("brand_folder_id"),10):
        raise ValueError("missing brand folder")
    groups={g.get("key") for g in index.get("groups",[]) if isinstance(g,dict)}
    if len(groups)<1:
        raise ValueError("missing asset groups")
    ids=set()
    for asset in index.get("candidate_files",[]):
        if type(asset)!=dict or not nonempty(asset.get("file_id"),10):
            raise ValueError("invalid asset ID")
        a=asset["file_id"]
        if a in ids:raise ValueError("duplicate asset ID")
        ids.add(a)
        if asset.get("group") not in groups or asset.get("url")!="https://drive.google.com/file/d/"+a+"/view":
            raise ValueError("invalid Drive source/group")
        status=asset.get("visual_review")
        if status not in ("not_done","reviewed"):
            raise ValueError("invalid visual review status")
        if status=="reviewed":
            for k in ("visual_verified_by","visual_verified_on","visual_evidence"):
                if not nonempty(asset.get(k),5):raise ValueError("visual review missing "+k)
            iso(asset["visual_verified_on"])
        elif any(k in asset for k in ("visual_verified_by","visual_verified_on","visual_evidence")):
            raise ValueError("visual evidence present without review")
        approve(asset.get("rights_verified"),asset,"rights_verified")
        approve(asset.get("menu_verified"),asset,"menu_verified")
    return {a["file_id"]:a for a in index["candidate_files"]}

def read_frontmatter(path):
    contents=Path(path).read_text(encoding="utf-8")
    match=re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n",contents,re.S)
    if not match:raise ValueError("missing YAML frontmatter")
    metadata=yaml.safe_load(match.group(1))
    if type(metadata)!=dict:raise ValueError("frontmatter must be mapping")
    return metadata

def validate_record(metadata,assets):
    if type(metadata)!=dict or set(metadata)!=REQUIRED:
        raise ValueError("wrong creative record fields")
    if metadata["schema_version"]!=1 or not re.fullmatch(r"BD-\d{8}-\d{3}",str(metadata["record_id"])):
        raise ValueError("invalid record id/version")
    day=iso(metadata["date"])
    if metadata["record_id"][3:11]!=day.strftime("%Y%m%d"):
        raise ValueError("record date mismatch")
    status=metadata["status"]
    if status not in STATUSES or metadata["platform"] not in PLATFORMS or not nonempty(metadata["format"]):
        raise ValueError("unknown status, platform or format")
    ideas=metadata["concepts"]
    if type(ideas)!=list or len(ideas)!=3:
        raise ValueError("exactly 3 concepts required")
    for c in ideas:
        if type(c)!=dict or set(c)!={"angle","hook","visual","score"} or c["angle"] not in ANGLES or not nonempty(c["hook"],5) or not nonempty(c["visual"],12) or type(c["score"]) is not int or not 1<=c["score"]<=5:
            raise ValueError("bad concept fields")
    if len({c["angle"] for c in ideas})!=3 or len({c["hook"].strip() for c in ideas})!=3 or len({c["visual"].strip() for c in ideas})!=3:
        raise ValueError("duplicate concept angles/hook/visual")
    if metadata["selected_angle"] not in {c["angle"] for c in ideas} or not nonempty(metadata["selection_reason"],15):
        raise ValueError("missing selected angle/rationale")
    ids=metadata["asset_ids"]
    if type(ids)!=list or len(ids)!=len(set(ids)) or any(x not in assets for x in ids):
        raise ValueError("unknown/duplicate asset source")
    kpi=metadata["primary_kpi"]
    if type(kpi)!=dict or set(kpi)!={"name","threshold","window_days","measurement_source"} or not nonempty(kpi["name"]) or type(kpi["threshold"]) not in (int,float) or kpi["threshold"]<=0 or type(kpi["window_days"]) is not int or not 1<=kpi["window_days"]<=90 or not nonempty(kpi["measurement_source"],8):
        raise ValueError("invalid primary KPI/target")
    approvals=metadata["approvals"]
    if type(approvals)!=list:raise ValueError("approvals must be list")
    for a in approvals:
        if type(a)!=dict or set(a)!={"by","date","evidence"} or not nonempty(a["by"]) or not nonempty(a["evidence"],8):
            raise ValueError("invalid approval evidence")
        iso(a["date"])
    gen=metadata["generated_asset_url"]
    if gen is not None and (not isinstance(gen,str) or not gen.startswith("https://") or "?" in gen):
        raise ValueError("unverified or signed generated asset location")
    publication=metadata["publication"]
    if publication is not None:
        if type(publication)!=dict or set(publication)!={"url","verified_by","verified_on"}:
            raise ValueError("publication missing verification")
        url=publication["url"]
        if not isinstance(url,str) or not re.match(r"^https://(?:www\.)?"+re.escape(PLATFORMS[metadata["platform"]])+r"/",url) or "?" in url or not nonempty(publication["verified_by"]) or iso(publication["verified_on"])<day:
            raise ValueError("invalid publication URL/date")
    stage=STATUSES.index(status)
    if stage>=2 and (not ids or any(assets[x]["visual_review"]!="reviewed" or not assets[x]["rights_verified"] or not assets[x]["menu_verified"] for x in ids)):
        raise ValueError("ready creative needs inspected, rights-approved current menu sources")
    if stage>=3 and not approvals:
        raise ValueError("owner approval evidence required")
    if stage>=4 and not gen:
        raise ValueError("produced creative needs real generated asset location")
    if stage>=5 and publication is None:
        raise ValueError("published creative needs verified platform URL")
    if stage<5 and publication is not None:
        raise ValueError("unpublished status cannot have publication")
    return True

def validate_production(directory,assets):
    found=[]
    for path in sorted(Path(directory).glob("*.md")):
        if path.name=="CREATIVE_RECORD_TEMPLATE.md":continue
        m=read_frontmatter(path)
        validate_record(m,assets)
        found.append(m["record_id"])
    if len(found)!=len(set(found)):raise ValueError("duplicate creative IDs")
    return len(found)

def main():
    try:
        assets=validate_assets(json.loads((ROOT/"assets/drive-source-index.json").read_text(encoding="utf-8")))
        total=validate_production(ROOT/"content/production",assets)
        print(f"PASS: {len(assets)} audited source entries, {total} tracked creative records")
        return 0
    except (ValueError,KeyError,TypeError,OSError,yaml.YAMLError) as exc:
        print("FAIL: creative validation: "+str(exc),file=sys.stderr)
        return 1

if __name__=="__main__":
    sys.exit(main())
