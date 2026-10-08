import argparse
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from scripts import daily_brief as d

SAMPLE = """# Ideas
| ID | Pillar | Format | Hook | Grounding | Primary goal |
|---|---|---|---|---|---|
| C001 | Food Desire | Reel | كبسة محسوبة | Asset | Awareness |
| C003 | Food Desire | Reel | مش بس فراخ ورز | Menu | Awareness |
| C006 | Education | Carousel | أحجام الوجبات | Portions | Consideration |
| C016 | Trust | Reel | من المطبخ | Prep assets | Trust |
"""

class DailyBriefTests(unittest.TestCase):
    def setUp(self):
        self.ideas = d.parse_backlog(SAMPLE)

    def test_priority(self):
        self.assertEqual(d.select_idea(self.ideas, [], "", "auto")["id"], "C003")

    def test_goal(self):
        self.assertEqual(d.select_idea(self.ideas, [], "", "trust")["id"], "C016")

    def test_published_requires_url(self):
        log = """### 2026-10-07 — CONTENT-C003
**Status:** Published
**Post URL:** https://www.instagram.com/reel/verified/
### 2026-10-08 — CONTENT-C006
**Status:** Published
**Post URL:
### 2026-10-08 — CONTENT-C001
**Status:** Scheduled
**Post URL:** https://example.org/
"""
        verified = d.confirmed_publications(log)
        self.assertEqual([v["id"] for v in verified], ["C003"])
        self.assertEqual(d.select_idea(self.ideas, verified, "", "auto")["id"], "C006")

    def test_published_repeat_rejected(self):
        with self.assertRaisesRegex(ValueError, "already published"):
            d.select_idea(self.ideas, [{"id": "C003", "date": "2026-10-08"}], "C003", "auto")

    def test_unknown_id(self):
        with self.assertRaisesRegex(ValueError, "Unknown idea"):
            d.select_idea(self.ideas, [], "C999", "auto")

    def test_all_exhausted(self):
        with self.assertRaisesRegex(ValueError, "No available"):
            d.select_idea(self.ideas, [{"id": x["id"]} for x in self.ideas], "", "auto")

    def test_packet_gates(self):
        packet = d.make_packet(self.ideas[0], "instagram", "2026-10-08", 0)
        self.assertEqual(packet["status"], "DRAFT_REVIEW_REQUIRED")
        self.assertEqual(len(packet["agents"]), 6)
        text = d.to_markdown(packet)
        self.assertIn("NOT PUBLISHED", text)
        self.assertIn("NO publishing", text)

    def test_offline_no_api(self):
        with tempfile.TemporaryDirectory() as out:
            args = argparse.Namespace(as_of="2026-10-08", channel="instagram",
                goal="auto", idea_id="", out_dir=out, ai=False, model="gpt-5")
            with patch.object(d, "IDEAS", Path(out)/"ideas.md"), \
                 patch.object(d, "PUBLISHED", Path(out)/"log.md"), \
                 patch.object(d, "ai_suggestions", side_effect=AssertionError("Unexpected AI")):
                (Path(out)/"ideas.md").write_text(SAMPLE, encoding="utf-8")
                (Path(out)/"log.md").write_text("# Empty", encoding="utf-8")
                self.assertEqual(d.run(args)["idea"]["id"], "C003")
                self.assertEqual(json.loads((Path(out)/"daily-brief.json").read_text())["status"], "DRAFT_REVIEW_REQUIRED")
                self.assertFalse((Path(out)/"ai-suggestions.md").exists())

    def test_key_required(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY"):
                d.ai_suggestions(d.make_packet(self.ideas[0], "instagram", "2026-10-08", 0), "gpt-5")

    def test_empty(self):
        with self.assertRaises(ValueError):
            d.parse_backlog("Nothing")

if __name__ == "__main__":
    unittest.main()
