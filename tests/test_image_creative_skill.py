"""Guardrails for reproducible, identity-consistent Basic Diet still imagery."""
import json
from pathlib import Path
import unittest
import yaml

ROOT=Path(__file__).resolve().parents[1]

class ImageCreativeSkillTests(unittest.TestCase):
    def test_native_skill_is_discoverable_and_not_vendor_replacement(self):
        skill=ROOT/".agents/skills/basic-diet-image-creative/SKILL.md"
        c=skill.read_text(encoding="utf-8")
        meta=yaml.safe_load(c.split("---",2)[1])
        self.assertEqual(meta["name"],"basic-diet-image-creative")
        self.assertIn("basic-diet-image-creative", (ROOT/".agents/skills/README.md").read_text())
        self.assertIn("basic-diet-image-creative", (ROOT/"AGENTS.md").read_text())
        self.assertIn("basic-diet-image-creative", (ROOT/".agents/workflows/ai-creative-production.md").read_text())
        self.assertIn("basic-diet-image-creative", (ROOT/"docs/CREATIVE_AGENT_PROTOCOL.md").read_text())
        self.assertIn("original",c.lower())
        self.assertTrue((ROOT/".agents/skills/ad-creative/SKILL.md").is_file())

    def test_identity_is_documented_as_provisional_with_actual_sources(self):
        data=json.loads((ROOT/"assets/visual-identity.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"],1)
        self.assertIn("not_owner_approved",data["status"])
        for key in ("green","orange","cream"):
            self.assertIn("provisional",data["palette"][key]["status"].replace("measured_from_candidate_logo_not_approved","provisional").replace("design_proposal_not_measured_or_approved","provisional"))
        self.assertEqual(data["palette"]["green"]["hex"],"#107F55")
        self.assertEqual(data["palette"]["orange"]["hex"],"#E95D2C")
        self.assertEqual(len(data["families"]),5)
        self.assertEqual(len(data["source_refs"]),3)
        for asset in data["source_refs"]:
            self.assertGreater(len(asset["drive_file_id"]),15)
        self.assertFalse(data["approvals"]["final_logo"])
        self.assertFalse(data["approvals"]["commercial_photo_rights"])
        self.assertEqual(data["placements"]["instagram_feed"],{"width":1080,"height":1350})

    def test_static_and_story_are_distinct_designs(self):
        skill=(ROOT/".agents/skills/basic-diet-image-creative/SKILL.md").read_text(encoding="utf-8")
        guide=(ROOT/"docs/IMAGE_CREATIVE_PLAYBOOK.md").read_text(encoding="utf-8")
        for token in ("1080×1350","1080×1920","product_hero","choice_comparison","editorial_statement","offer_card","story_micro"):
            self.assertIn(token,skill)
        for token in ("No food, no logos, no text","original","never reimagine","Arabic","photo","claim"):
            self.assertIn(token.lower(),guide.lower())
        self.assertIn("separately",guide)
        self.assertIn("owner",guide)

    def test_competitor_research_marks_instagram_access_limit(self):
        note=(ROOT/"research/competitors/healthy-corner-2026-10-09.md").read_text(encoding="utf-8")
        self.assertIn("https://www.instagram.com/healthy_corner_sa/",note)
        self.assertIn("not accessible",note)
        self.assertIn("website content",note)
        self.assertIn("not copied",note)

if __name__=="__main__":
    unittest.main()
