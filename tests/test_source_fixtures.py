import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SourceFixtureTests(unittest.TestCase):
    def test_declared_files_match_csv_headers_and_rows(self):
        contract = json.loads((ROOT / "data-contract.json").read_text(encoding="utf-8"))
        self.assertTrue(contract["data_is_synthetic"])
        self.assertGreaterEqual(len(contract["files"]), 3)
        for name, expected in contract["files"].items():
            with (ROOT / "data" / name).open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                rows = list(reader)
            self.assertEqual(reader.fieldnames, expected["columns"], name)
            self.assertEqual(len(rows), expected["row_count"], name)
            self.assertTrue(rows, name)
            self.assertTrue(all(all(value is not None for value in row.values()) for row in rows), name)


if __name__ == "__main__":
    unittest.main()
