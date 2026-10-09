#!/usr/bin/env python3
"""Semantic/evidence guardrails for Marketing OS creatives.

CAUTION: text metadata cannot authenticate a reviewer. Protected branch rules and
CODEOWNERS-approved changes are needed for independent human authorization.
"""
from __future__ import annotations
import datetime as dt
import json
import re
from pathlib import Path
import sys
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.lint_copy import check_copy

ROOT = Path(__file__).resolve().parents[1]
ANGLES = {"food_desire", "convenience", "choice", "trust", "education", "offer", "community", "behind_scenes"}
STATUSES = ("CONCEPT_DRAFT", "NEEDS_ASSET_VISUAL_REVIEW", "READY_FOR_HUMAN_APPROVAL", "APPROVED_BY_OWNER", "PRODUCED", "PUBLISHED_VERIFIED")
PLATFORMS = {"instagram": "instagram.com", "facebook": "facebook.com", "tiktok": "tiktok.com", "snapchat": "snapchat.com"}
REQUIRED = {
    "schema_version","record_id","date","status","platform","format","concepts",
    "selected_angle","selection_reason","asset_ids","brand_logo_asset_id","copy",
    "primary_kpi","approvals","generated_asset_url","publication",
}
SCORES = {"brand_fit", "hook", "asset_fit", "execution"}


def nonempty(x, n=3):
    return isinstance(x, str) and len(x.strip()) >= n


def iso(value):
    if not isinstance(value, str):
        raise ValueError("date should be a string YYYY-MM-DD")
    try:
        date = dt.date.fromisoformat(value)
    except ValueError as ex:
        raise ValueError("invalid YYYY-MM-DD date") from ex
    if date.isoformat() != value or date > dt.datetime.now(dt.timezone.utc).date():
        raise ValueError("future or non-canonical date")
    return date


def evidence(asset, prefix):
    keys = (prefix+"_by", prefix+"_on", prefix+"_evidence")
    for key in keys:
        if not nonempty(asset.get(key), 5):
            raise ValueError("missing signed-off evidence field: "+key)
    iso(asset[prefix+"_on"])


def approval(asset, prefix):
    if type(asset.get(prefix)) is not bool:
        raise ValueError(prefix+" must be boolean")
    if asset[prefix]:
        if asset.get("visual_review") != "human_reviewed":
            raise ValueError(prefix+" needs separate human visual review")
        evidence(asset, prefix)


def validate_assets(index):
    if not isinstance(index, dict) or index.get("schema_version") != 1:
        raise ValueError("invalid asset source schema")
    iso(index.get("checked_at"))
    if not nonempty(index.get("brand_folder_id"), 10):
        raise ValueError("missing brand folder")
    groups = {g.get("key") for g in index.get("groups", []) if isinstance(g, dict)}
    if not groups:
        raise ValueError("no source groups")
    ids = {}
    for asset in index.get("candidate_files", []):
        if type(asset) is not dict or not nonempty(asset.get("file_id"), 10):
            raise ValueError("invalid Drive asset ID")
        fid = asset["file_id"]
        if fid in ids or asset.get("group") not in groups or asset.get("url") != "https://drive.google.com/file/d/"+fid+"/view":
            raise ValueError("duplicate, unknown group or invalid canonical Drive reference")
        status = asset.get("visual_review")
        if status not in ("not_done", "ai_reviewed", "human_reviewed"):
            raise ValueError("unknown visual_review status")
        if status != "not_done":
            evidence(asset, "visual_verified")
        elif any(k in asset for k in ("visual_verified_by","visual_verified_on","visual_verified_evidence","visual_evidence")):
            raise ValueError("visual verification evidence without inspection")
        if status == "human_reviewed":
            evidence(asset, "human_visual_verified")
        elif any(k in asset for k in ("human_visual_verified_by","human_visual_verified_on","human_visual_verified_evidence")):
            raise ValueError("human review evidence without human_reviewed")
        approval(asset, "rights_verified")
        approval(asset, "menu_verified")
        ids[fid] = asset
    return ids


def read_frontmatter(path):
    content = Path(path).read_text(encoding="utf-8")
    found = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", content, flags=re.S)
    if not found:
        raise ValueError("missing YAML frontmatter")
    obj = yaml.safe_load(found.group(1))
    if type(obj) is not dict:
        raise ValueError("invalid YAML metadata")
    return obj


def validate_record(m, assets, social=None):
    if type(m) is not dict or set(m) != REQUIRED:
        raise ValueError("missing or extra creative record metadata")
    if m["schema_version"] != 2 or not re.fullmatch(r"BD-\d{8}-\d{3}", str(m["record_id"])):
        raise ValueError("invalid creative record ID/version")
    day = iso(m["date"])
    if m["record_id"][3:11] != day.strftime("%Y%m%d"):
        raise ValueError("record date/id mismatch")
    stage = m["status"]
    if stage not in STATUSES or m["platform"] not in PLATFORMS or not nonempty(m["format"]):
        raise ValueError("invalid status, channel or creative format")
    concepts = m["concepts"]
    if type(concepts) is not list or len(concepts) != 3:
        raise ValueError("exactly 3 creative concepts required")
    hooks, visuals, angles, feasible = set(), set(), set(), set()
    for idea in concepts:
        keys = {"angle","hook","visual","asset_ids","feasible_now","rejected_reason","score_breakdown"}
        if type(idea) is not dict or set(idea) != keys:
            raise ValueError("invalid concept record fields")
        if idea["angle"] not in ANGLES or not nonempty(idea["hook"], 5) or not nonempty(idea["visual"], 12):
            raise ValueError("invalid creative angle/hook/visual")
        for name, seen in (("hook",hooks),("visual",visuals),("angle",angles)):
            value = idea[name].strip()
            if value in seen:
                raise ValueError("duplicate concept angle/hook/visual")
            seen.add(value)
        subset = idea["asset_ids"]
        if type(subset) is not list or len(subset) != len(set(subset)) or any(x not in assets for x in subset):
            raise ValueError("invalid concept source asset_ids")
        scores = idea["score_breakdown"]
        if type(scores) is not dict or set(scores) != SCORES or any(type(x) is not int or not 1 <= x <= 5 for x in scores.values()):
            raise ValueError("score_breakdown must include four 1-5 rubric dimensions")
        if type(idea["feasible_now"]) is not bool:
            raise ValueError("feasible_now must be bool")
        if idea["feasible_now"]:
            if not subset or any(assets[x]["visual_review"]=="not_done" for x in subset) or idea["rejected_reason"] is not None:
                raise ValueError("feasible concept needs visually inspected existing source and no rejection")
            feasible.add(idea["angle"])
        elif not nonempty(idea["rejected_reason"], 12):
            raise ValueError("infeasible concept requires rejection reason")
    if m["selected_angle"] not in feasible or not nonempty(m["selection_reason"], 15):
        raise ValueError("selected concept must be feasible as draft with reason")
    ids = m["asset_ids"]
    selected = next(x for x in concepts if x["angle"]==m["selected_angle"])
    if type(ids) is not list or len(ids)!=len(set(ids)) or not ids or set(ids)!=set(selected["asset_ids"]):
        raise ValueError("selected creative source ids must match chosen concept")
    logo = m["brand_logo_asset_id"]
    if logo is not None and (logo not in assets or assets[logo]["group"]!="logos"):
        raise ValueError("invalid official logo reference")
    copy = m["copy"]
    if type(copy) is not dict or set(copy)!={"caption","on_design_text","cta","stories"} or any(not nonempty(copy[k], 2) for k in ("caption","on_design_text","cta")) or type(copy["stories"]) is not list or len(copy["stories"])<2:
        raise ValueError("missing executable copy package")
    check_copy(m)
    kpi = m["primary_kpi"]
    if type(kpi) is not dict or set(kpi)!={"name","threshold","baseline","window_days","measurement_source","source_status","evidence"}:
        raise ValueError("invalid primary KPI fields")
    if not nonempty(kpi["name"]) or type(kpi["window_days"]) is not int or not 1<=kpi["window_days"]<=90 or not nonempty(kpi["measurement_source"], 8):
        raise ValueError("invalid primary KPI definition")
    if kpi["source_status"] not in ("disconnected","connected","manual_verified"):
        raise ValueError("invalid KPI source status")
    if kpi["source_status"]=="disconnected":
        if kpi["threshold"] is not None or kpi["baseline"] is not None or kpi["evidence"] is not None:
            raise ValueError("no fabricated KPI threshold/baseline/evidence when disconnected")
    else:
        if type(kpi["threshold"]) not in (int,float) or kpi["threshold"]<=0 or type(kpi["baseline"]) not in (int,float) or kpi["baseline"]<0 or not nonempty(kpi["evidence"],8):
            raise ValueError("connected KPI requires actual measured baseline, target and evidence")
    if type(m["approvals"]) is not list:
        raise ValueError("approvals must be list")
    for row in m["approvals"]:
        if type(row) is not dict or set(row)!={"by","date","evidence"} or not nonempty(row["by"]) or not nonempty(row["evidence"],8):
            raise ValueError("bad approval evidence")
        iso(row["date"])
    gen = m["generated_asset_url"]
    if gen is not None and (not isinstance(gen,str) or not gen.startswith("https://") or "?" in gen):
        raise ValueError("invalid produced asset URL")
    pub = m["publication"]
    if pub is not None:
        if type(pub) is not dict or set(pub)!={"url","verified_by","verified_on"}:
            raise ValueError("publication requires verified URL evidence")
        if not isinstance(pub["url"],str) or not re.match(r"^https://(?:www\.)?"+re.escape(PLATFORMS[m["platform"]])+r"/",pub["url"]) or "?" in pub["url"] or not nonempty(pub["verified_by"]) or iso(pub["verified_on"])<day:
            raise ValueError("invalid publication details")
    if STATUSES.index(stage) >= 2:
        if kpi["source_status"]=="disconnected":
            raise ValueError("not publish-ready: metric source disconnected")
        if social is not None and kpi["source_status"]=="connected":
            matching=[c for c in social.get("connections",[]) if c.get("platform")==m["platform"]]
            if not matching or not matching[0].get("metrics_enabled") or matching[0].get("status")!="connected":
                raise ValueError("metric source not connected in social provider registry")
        if any(assets[fid]["visual_review"]!="human_reviewed" or not assets[fid]["rights_verified"] or not assets[fid]["menu_verified"] for fid in ids):
            raise ValueError("food source requires owner-reviewed pixels, usage rights and current menu")
        if not logo or assets[logo]["visual_review"]!="human_reviewed" or not assets[logo]["rights_verified"]:
            raise ValueError("official logo still needs independent human review and rights")
    if STATUSES.index(stage) >= 3 and not m["approvals"]:
        raise ValueError("missing real owner approval evidence")
    if STATUSES.index(stage) >= 4 and not gen:
        raise ValueError("missing produced media source")
    if STATUSES.index(stage) >= 5 and pub is None:
        raise ValueError("published status without canonical verified post URL")
    if STATUSES.index(stage)<5 and pub is not None:
        raise ValueError("publication set on non-published creative")
    return True


def validate_production(directory, assets, social=None):
    ids = set()
    n = 0
    for path in sorted(Path(directory).glob("*.md")):
        if path.name=="CREATIVE_RECORD_TEMPLATE.md":
            continue
        record = read_frontmatter(path)
        validate_record(record, assets, social)
        if record["record_id"] in ids:
            raise ValueError("duplicate creative ID")
        ids.add(record["record_id"])
        n += 1
    return n


def main():
    try:
        assets = validate_assets(json.loads((ROOT/"assets/drive-source-index.json").read_text(encoding="utf-8")))
        social = json.loads((ROOT/"data/sources/social-connections.json").read_text(encoding="utf-8"))
        count = validate_production(ROOT/"content/production", assets, social)
        print(f"PASS: {len(assets)} asset sources, {count} tracked AI creative drafts")
        return 0
    except (ValueError,KeyError,TypeError,OSError,yaml.YAMLError) as exc:
        print("FAIL: creative validation:", str(exc), file=sys.stderr)
        return 1


if __name__=="__main__":
    sys.exit(main())
