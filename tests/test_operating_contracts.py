from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import yaml
from scripts import daily_brief as d
from scripts import validate_skills as skills
from scripts.validate_operations import workflow_errors


class OperatingContractsTests(unittest.TestCase):
    def test_fresh_session_bootstrap_and_skill_discovery(self):
        agents=(d.ROOT/'AGENTS.md').read_text()
        self.assertIn('AGENTS.md → STATE.md → Native Basic Diet Skill → Task-Specific Skills → Verified Knowledge and Data',agents)
        for path in ('STATE.md','.agents/skills/basic-diet-marketing/SKILL.md','.agents/skills/README.md','docs/PHASE3_RUNBOOK.md'):
            self.assertIn(path,agents)
            self.assertTrue((d.ROOT/path).is_file())
        index=(d.ROOT/'.agents/skills/README.md').read_text()
        for path in (d.ROOT/'.agents/skills').glob('*/SKILL.md'):
            meta=yaml.safe_load(path.read_text().split('---',2)[1])
            self.assertEqual(meta['name'],path.parent.name)
            self.assertIn(path.parent.name,index)
            self.assertIsInstance(meta['description'],str)
        self.assertTrue((d.ROOT/'.agents/product-marketing.md').is_file())

    def test_skill_checker_rejects_broken_native_yaml_and_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            shutil.copytree(d.ROOT/'.agents',root/'.agents')
            (root/'docs').mkdir()
            shutil.copy(d.ROOT/'docs/UPSTREAM_MANIFEST.json',root/'docs/UPSTREAM_MANIFEST.json')
            (root/'knowledge').mkdir()
            shutil.copy(d.ROOT/'knowledge/offers-pricing.md',root/'knowledge/offers-pricing.md')
            with patch.object(skills,'ROOT',root),patch.object(skills,'MANIFEST',root/'docs/UPSTREAM_MANIFEST.json'),redirect_stdout(io.StringIO()):
                self.assertEqual(skills.main(),0)
                native=root/'.agents/skills/basic-diet-marketing/SKILL.md'
                original=native.read_text()
                native.write_text(original.replace('name: basic-diet-marketing','name: [broken'))
                self.assertEqual(skills.main(),1)
                native.write_text(original+'\n[broken](references/absent.md)\n')
                self.assertEqual(skills.main(),1)

    def test_workflow_yaml_permissions_and_all_change_coverage(self):
        for path in (d.ROOT/'.github/workflows').glob('*.yml'):
            self.assertEqual(workflow_errors(path),[])

    def test_workflow_policy_detects_escalation_injection_and_schedule(self):
        source=d.ROOT/'.github/workflows/daily-content-brief.yml'
        original=source.read_text()
        mutations=[original.replace('contents: read','contents: write'),
                   original.replace('actions/checkout@11d5960a326750d5838078e36cf38b85af677262','actions/checkout@v4'),
                   original.replace('persist-credentials: false','persist-credentials: true'),
                   original.replace('run: python3 scripts/daily_brief.py','run: echo ${{ inputs.idea_id }}; python3 scripts/daily_brief.py'),
                   original.replace('  workflow_dispatch:', '  schedule: []\n  workflow_dispatch:'),
                   original.replace('if: ${{ inputs.use_ai }}','if: ${{ always() }}')]
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/source.name
            for text in mutations:
                path.write_text(text)
                self.assertTrue(workflow_errors(path))

    def test_optional_missing_vendor_links_have_explicit_fallbacks(self):
        routes=json.loads((d.ROOT/'.agents/skill-overrides.json').read_text())['missing_reference_routes']
        self.assertEqual(len(routes),2)
        for route in routes:
            self.assertTrue((d.ROOT/route['source']).is_file())
            self.assertTrue((d.ROOT/route['fallback']).is_file())
            self.assertIn('b9ba399dd88b082b926e261e8ccfb843d20aa066',route['upstream'])

class SecretScanTests(unittest.TestCase):
    def test_credential_markers_are_detected_without_echoing_values(self):
        from scripts.security import contains_credential
        for value in ['ghp_'+'a'*36,'sk-proj-'+'A'*40,'AKIA'+'A'*16,
                      'https://storage.example/file?X-Amz-Signature='+'a'*32]:
            self.assertTrue(contains_credential(value))
        self.assertFalse(contains_credential('OPENAI_API_KEY is configured via secret manager'))

class HistoricalMemoryTests(unittest.TestCase):
    def test_working_memory_can_evolve_but_archive_is_immutable(self):
        import re
        from scripts import verify_migration as migration
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            manifest=d.ROOT/'docs/MIGRATION.md'
            (root/'docs').mkdir()
            (root/'docs/MIGRATION.md').write_bytes(manifest.read_bytes())
            for line in manifest.read_text().splitlines():
                if not re.match(r'^\| `(?:marketing|skills)/',line):continue
                fields=re.findall(r'`([^`]+)`',line)
                paths=fields[1:3] if len(fields)==4 else fields[1:2]
                for relative in paths:
                    dest=root/relative;dest.parent.mkdir(parents=True,exist_ok=True)
                    dest.write_bytes((d.ROOT/relative).read_bytes())
            with patch.object(migration,'ROOT',root),patch.object(migration,'MANIFEST',root/'docs/MIGRATION.md'),redirect_stdout(io.StringIO()):
                (root/'content/winners.md').write_text('New dated verified learning belongs here')
                self.assertEqual(migration.run(),0)
                (root/'archive/basicdiet145-2026-10-07/marketing/content/winners.md').write_text('Changed history')
                self.assertEqual(migration.run(),1)
