import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_1 import safe_divide

def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5

def test_safe_divide_zero():
    assert safe_divide(10, 0) is None
