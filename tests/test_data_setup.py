import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "NIFTY50_data.csv"
NOTEBOOK = ROOT / "bootstrap_nifty50_ci.ipynb"


class RepositorySetupTests(unittest.TestCase):
    def test_notebook_has_portable_dataset_path_and_clear_missing_data_error(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        code = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook["cells"]
            if cell.get("cell_type") == "code"
        )
        self.assertIn('Path.cwd() / "data" / "NIFTY50_data.csv"', code)
        self.assertNotIn(r"C:\Users\vyash", code)
        self.assertIn("FileNotFoundError", code)
        self.assertIn("dataset you are licensed to use", code)

    def test_notebook_outputs_are_cleared(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        code_cells = [c for c in notebook["cells"] if c.get("cell_type") == "code"]
        self.assertTrue(code_cells)
        self.assertTrue(all(c.get("execution_count") is None for c in code_cells))
        self.assertTrue(all(not c.get("outputs") for c in code_cells))

    def test_unverified_raw_dataset_is_not_bundled(self):
        self.assertFalse(DATA.exists(), "Do not redistribute this source data without confirming rights")


if __name__ == "__main__":
    unittest.main()
