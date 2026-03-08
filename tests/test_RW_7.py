import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_7 import divide

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_zero():
    assert divide(10, 0) is None
