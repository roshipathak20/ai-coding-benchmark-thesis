import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_10 import sum_range

def test_sum_range_basic():
    assert sum_range(5) == 15

def test_sum_range_zero():
    assert sum_range(0) == 0
