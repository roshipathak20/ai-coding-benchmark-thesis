import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_6 import csv_average

def test_csv_average_basic(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("name,score\nA,10\nB,20\nC,30\n", encoding="utf-8")
    assert csv_average(str(file_path), "score") == 20.0

def test_missing_column(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("name,score\nA,10\n", encoding="utf-8")
    try:
        csv_average(str(file_path), "age")
        assert False
    except ValueError:
        assert True
