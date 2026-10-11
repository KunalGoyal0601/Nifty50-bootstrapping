import json
from pathlib import Path
import unittest

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "NIFTY50_data.csv"
NOTEBOOK = ROOT / "bootstrap_nifty50_ci.ipynb"


class RepositorySetupTests(unittest.TestCase):
    def test_committed_dataset_has_expected_structure(self):
        self.assertTrue(DATA.is_file(), f"Missing dataset: {DATA}")
        raw = pd.read_csv(DATA, header=[0, 1])
        self.assertEqual(len(raw.columns), 6)
        self.assertGreater(len(raw), 100)
        raw.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
        cleaned = raw[raw["Date"] != "Date"].copy()
        cleaned["Date"] = pd.to_datetime(cleaned["Date"], errors="coerce")
        cleaned["Close"] = pd.to_numeric(cleaned["Close"], errors="coerce")
        cleaned = cleaned.dropna(subset=["Date", "Close"])
        self.assertGreater(len(cleaned), 100)
        self.assertTrue((cleaned["Close"] > 0).all())

    def test_notebook_uses_repo_data_and_consistent_output_folder(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        code = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook["cells"]
            if cell.get("cell_type") == "code"
        )
        self.assertIn('Path.cwd() / "data" / "NIFTY50_data.csv"', code)
        self.assertNotIn(r"C:\Users\vyash", code)
        self.assertNotIn("outputs/", code)
        self.assertIn("output/01_price_trend.png", code)


if __name__ == "__main__":
    unittest.main()
