#!/usr/bin/env python3
"""Check operating contracts, structured records and workflow permissions offline."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import daily_brief as d
from scripts.records import load_ideas, load_publications, load_runs, load_performance, parse_backlog, read_required


def workflow_errors(path):
    # BaseLoader preserves YAML 1.2 'on'; values are strings for explicit comparisons.
    try:
        obj = yaml.load(path.read_text(), Loader=yaml.BaseLoader)
    except yaml.YAMLError:
        return ['Invalid YAML']
    errors=[]
    if not isinstance(obj,dict):
        return ['Workflow must be a mapping']
    if obj.get('permissions') != {'contents':'read'}:
        errors.append('Workflow must have contents: read only')
    triggers=obj.get('on',{})
    if path.name=='daily-content-brief.yml' and set(triggers) != {'workflow_dispatch'}:
        errors.append('Daily workflow must remain dispatch-only')
    if path.name=='quality.yml':
        if set(triggers) != {'push','pull_request'} or any('paths' in (v or {}) for v in triggers.values()):
            errors.append('Quality must cover all source/data/instruction changes')
    for job in obj.get('jobs',{}).values():
        if 'permissions' in job and job['permissions'] != {'contents':'read'}:
            errors.append('Job escalates permissions')
        if 'timeout-minutes' not in job or int(job['timeout-minutes']) > 10:
            errors.append('Missing/broad timeout')
        for step in job.get('steps',[]):
            if 'uses' in step and not re.fullmatch(r'actions/[\w-]+@[a-f0-9]{40}',step['uses']):
                errors.append('Action must be pinned by full SHA')
            if step.get('uses','').startswith('actions/checkout@') and step.get('with',{}).get('persist-credentials') != 'false':
                errors.append('Checkout persists credentials')
            if '${{' in step.get('run',''):
                errors.append('Do not interpolate expressions into shell code')
            env=step.get('env',{})
            if any('secrets.' in str(v) for v in env.values()) and step.get('if') != '${{ inputs.use_ai }}':
                errors.append('Secrets must be limited to explicit AI step')
    return errors


def main():
    ideas=load_ideas(d.IDEAS)
    original=parse_backlog(read_required(ROOT/'archive/basicdiet145-2026-10-07/marketing/content/backlog.md'))
    if any(row not in ideas for row in original):
        raise ValueError('Original 30 ideas changed or lost')
    d.profiles_for(ideas)
    today=d.saudi_today()
    pubs=load_publications(d.PUBLICATIONS,d.PUBLISHED,ideas,today)
    load_runs(d.RUNS,ideas,today)
    load_performance(d.PERFORMANCE,pubs,today)
    for path in (ROOT/'.github/workflows').glob('*.yml'):
        errors=workflow_errors(path)
        if errors:
            raise ValueError(f'{path.name}: {errors}')
    # Every new session must be able to traverse this chain locally.
    for path in d.CONTEXT:
        read_required(ROOT/path)
    for role in ['research','strategy','creative','analytics','media-buyer','operations']:
        text=read_required(ROOT/'agents'/f'{role}.md')
        for field in ('Inputs','Output','Skills','Permissions','Verification','Handoff'):
            if field not in text:
                raise ValueError(f'Missing {field} in role {role}')
    print('PASS: 30 original ideas, structured records, six role contracts, bootstrap and workflow policy')
    return 0


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError,ValueError) as exc:
        print(f'FAIL: {exc}',file=sys.stderr)
        raise SystemExit(1)
