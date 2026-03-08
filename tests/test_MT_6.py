import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_6 import parse_int_list

def test_parse_valid_and_invalid():
    assert parse_int_list("1, 2, x, 3") == [1, 2, 3]

def test_parse_empty():
    assert parse_int_list("") == []
