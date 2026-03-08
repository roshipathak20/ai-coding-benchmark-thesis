import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_3 import is_balanced

def test_balanced_true():
    assert is_balanced("(())") is True

def test_balanced_false():
    assert is_balanced("(()") is False

def test_empty():
    assert is_balanced("") is True
