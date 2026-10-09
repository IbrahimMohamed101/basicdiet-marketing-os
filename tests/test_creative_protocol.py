import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CreativeAgentProtocolTests(unittest.TestCase):
    def test_mandatory_read_order_and_skills(self):
        gate = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        native = (ROOT / ".agents/skills/basic-diet-marketing/SKILL.md").read_text(encoding="utf-8")
        protocol = (ROOT / "docs/CREATIVE_AGENT_PROTOCOL.md").read_text(encoding="utf-8")
        workflow = (ROOT / ".agents/workflows/ai-creative-production.md").read_text(encoding="utf-8")
        for required in ("STATE.md", "docs/CREATIVE_AGENT_PROTOCOL.md", "content-strategy", "social", "ad-creative", "docs/GOOGLE_FLOW_PRODUCTION.md"):
            self.assertIn(required, gate)
            self.assertIn(required, protocol)
        self.assertIn("docs/CREATIVE_AGENT_PROTOCOL.md", native)
        self.assertIn("assets/drive-source-index.json", native)
        self.assertIn("three distinct ideas", workflow)
        for skill in ("content-strategy", "social", "ad-creative", "video", "storyboard-to-video", "ads", "attribution"):
            self.assertTrue((ROOT / f".agents/skills/{skill}/SKILL.md").is_file())
        self.assertIn("not", protocol.lower())

    def test_google_flow_fidelity_and_approval(self):
        prompt = (ROOT / "docs/GOOGLE_FLOW_PRODUCTION.md").read_text(encoding="utf-8")
        for required in ("video/SKILL.md", "storyboard-to-video/SKILL.md", "PRODUCT FIDELITY", "No AI-generated Arabic lettering", "negative"):
            self.assertIn(required.lower(), prompt.lower())

    def test_index_is_real_drive_metadata_with_unique_exact_ids(self):
        x = json.loads((ROOT / "assets/drive-source-index.json").read_text(encoding="utf-8"))
        self.assertEqual(x["schema_version"], 1)
        self.assertEqual(x["checked_at"], "2026-10-09")
        self.assertEqual(x["brand_folder_id"], "1ZplIhzIZKcK5ZCoe454exU445cL-Vhz-")
        groups = {g["key"] for g in x["groups"]}
        self.assertGreaterEqual(len(groups), 8)
        ids = [v["file_id"] for v in x["candidate_files"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 15)
        for v in x["candidate_files"]:
            self.assertIn(v["group"], groups)
            self.assertEqual(v["url"], "https://drive.google.com/file/d/"+v["file_id"]+"/view")
            self.assertFalse(v["rights_verified"])
            self.assertFalse(v["menu_verified"])
            self.assertEqual(v["visual_review"], "not_done")

    def test_memory_requires_evidence_not_published_template(self):
        t=(ROOT/"content/production/CREATIVE_RECORD_TEMPLATE.md").read_text(encoding="utf-8")
        for required in ("Owner approval evidence", "Drive folder/file ID", "Publication", "Performance/results", "Human checks needed"):
            self.assertIn(required,t)

if __name__ == "__main__":
    unittest.main()
