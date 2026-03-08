import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import solutions.RW_10 as rw10

def test_test_file_has_pytest_tests():
    file_text = open(rw10.__file__, "r", encoding="utf-8").read()
    assert "def test_" in file_text
