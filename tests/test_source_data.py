import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SourceDataTests(unittest.TestCase):
    def test_read_all_listed_sources(self):
        contract = json.loads((ROOT / "data-contract.json").read_text(encoding="utf-8"))
        self.assertTrue(contract["data_is_synthetic"])
        self.assertEqual(sorted(contract["files"]), sorted(path.name for path in (ROOT / "data").glob("*.csv")))
        for name, expected in contract["files"].items():
            with self.subTest(source=name), (ROOT / "data" / name).open(encoding="utf-8", newline="") as stream:
                reader = csv.reader(stream, strict=True)
                columns = next(reader)
                rows = list(reader)
                self.assertEqual(columns, expected["columns"])
                self.assertEqual(len(set(columns)), len(columns))
                self.assertEqual(len(rows), expected["row_count"])
                self.assertTrue(all(len(row) == len(columns) and row[0] for row in rows))
