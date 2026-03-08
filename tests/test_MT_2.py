import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_2 import is_even

def test_even_true():
    assert is_even(4) is True

def test_even_false():
    assert is_even(5) is False
