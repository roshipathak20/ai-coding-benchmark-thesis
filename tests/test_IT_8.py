import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_8 import json_roundtrip

def test_json_roundtrip(tmp_path):
    file_path = tmp_path / "sample.json"
    data = {"name": "Roshi", "age": 25}
    assert json_roundtrip(str(file_path), data) == data
