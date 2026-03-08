import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_6 import csv_column_averages

def test_csv_column_averages(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("a,b\n1,2\n3,4\n", encoding="utf-8")
    result = csv_column_averages(str(file_path))
    assert result == {"a": 2.0, "b": 3.0}
