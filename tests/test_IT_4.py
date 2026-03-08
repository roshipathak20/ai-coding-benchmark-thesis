import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_4 import word_frequency

def test_basic_frequency():
    assert word_frequency("apple banana apple") == {"apple": 2, "banana": 1}

def test_case_insensitive():
    assert word_frequency("Hello hello") == {"hello": 2}

def test_empty():
    assert word_frequency("") == {}
