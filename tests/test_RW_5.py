import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_5 import top_words

def test_top_words(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello hello world world world", encoding="utf-8")
    result = top_words(str(file_path))
    assert result[0][0] == "world"
    assert result[0][1] == 3
