import json
import unittest
from pathlib import Path

from src.data_contract import load_input_bundle


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SCHEMA = json.loads((DATA / "schema.json").read_text(encoding="utf-8"))


class FixtureContractTests(unittest.TestCase):
    def test_every_declared_file_is_valid_json(self):
        for filename, required in SCHEMA["files"].items():
            payload = json.loads((DATA / filename).read_text(encoding="utf-8"))
            self.assertTrue(set(required).issubset(payload))

    def test_fixture_has_synthetic_event_marker(self):
        self.assertEqual(SCHEMA["event"], "synthetic-heritage-workshop-v1")

    def test_input_bundle_matches_declared_contract(self):
        bundle = load_input_bundle(ROOT)
        self.assertEqual(set(bundle), set(SCHEMA["files"]))


if __name__ == "__main__":
    unittest.main()
