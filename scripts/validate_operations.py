#!/usr/bin/env python3
"""Validate agent operating memory and read-only / OIDC workflow contracts."""
from pathlib import Path
import re
import sys
import yaml

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts import daily_brief as d
from scripts.records import load_ideas,load_publications,load_runs,load_performance,parse_backlog,read_required

def workflow_errors(path):
    try:
        doc=yaml.load(path.read_text(encoding="utf-8"),Loader=yaml.BaseLoader)
    except (yaml.YAMLError, OSError):
        return ["Invalid YAML"]
    if not isinstance(doc,dict):
        return ["Workflow must be a mapping"]
    special=path.name=="sync-commerce.yml"
    permissions={"contents":"write","id-token":"write"} if special else {"contents":"read"}
    errors=[]
    if doc.get("permissions") != permissions:
        errors.append("Workflow must have limited permissions")
    events=doc.get("on",{})
    if path.name=="daily-content-brief.yml" and set(events)!={"workflow_dispatch"}:
        errors.append("Daily creative workflow must remain manual")
    if path.name=="quality.yml":
        if set(events)!={"push","pull_request"} or any("paths" in (v or {}) for v in events.values()):
            errors.append("Quality checks must cover all changes")
    if special:
        if set(events)!={"workflow_dispatch","push","schedule"}:
            errors.append("Commerce sync triggers mismatch")
        if events.get("push",{}).get("branches")!=["main"] or events.get("push",{}).get("paths")!=[".github/workflows/sync-commerce.yml"]:
            errors.append("Commerce sync push scope mismatch")
        if len(doc.get("jobs",{}))!=1:
            errors.append("Commerce sync must have exactly one job")
    for job in doc.get("jobs",{}).values():
        if special and job.get("if")!="github.ref == 'refs/heads/main'":
            errors.append("Commerce sync must enforce main branch")
        if job.get("permissions",permissions)!=permissions:
            errors.append("Unexpected job permissions")
        try:
            timeout=int(job.get("timeout-minutes",99))
        except (ValueError,TypeError):
            timeout=99
        if timeout>10:
            errors.append("Missing/broad timeout")
        for step in job.get("steps",[]):
            if "uses" in step and not re.fullmatch(r"actions/[\w-]+@[a-f0-9]{40}",step["uses"]):
                errors.append("Actions not pinned")
            if step.get("uses","").startswith("actions/checkout@") and step.get("with",{}).get("persist-credentials")!="false":
                errors.append("Checkout credentials must not persist")
            if "$"+"{{" in step.get("run",""):
                errors.append("Do not interpolate actions expressions into shell")
            if any(("se"+"crets.") in str(v) for v in step.get("env",{}).values()) and step.get("if")!="$"+"{{ inputs.use_ai }}":
                errors.append("Unexpected secret exposure")
    return errors

def main():
    ideas=load_ideas(d.IDEAS)
    original=parse_backlog(read_required(ROOT/"archive/basicdiet145-2026-10-07/marketing/content/backlog.md"))
    if any(row not in ideas for row in original):
        raise ValueError("Original 30 ideas changed")
    d.profiles_for(ideas)
    now=d.saudi_today()
    pubs=load_publications(d.PUBLICATIONS,d.PUBLISHED,ideas,now)
    load_runs(d.RUNS,ideas,now)
    load_performance(d.PERFORMANCE,pubs,now)
    for path in (ROOT/".github/workflows").glob("*.yml"):
        problems=workflow_errors(path)
        if problems:raise ValueError(str(path.name)+": "+str(problems))
    for path in d.CONTEXT:read_required(ROOT/path)
    for name in ("research","strategy","creative","analytics","media-buyer","operations"):
        content=read_required(ROOT/"agents"/(name+".md"))
        for field in ("Inputs","Output","Skills","Permissions","Verification","Handoff"):
            if field not in content:raise ValueError("Missing role contract: "+name+"/"+field)
    print("PASS: operating records, roles, source integrity and scoped workflows")
    return 0

if __name__=="__main__":
    try:
        sys.exit(main())
    except (OSError,ValueError) as err:
        print("FAIL:",err,file=sys.stderr)
        sys.exit(1)
