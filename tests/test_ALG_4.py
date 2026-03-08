import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_4 import max_subarray

def test_max_subarray_basic():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_single():
    assert max_subarray([1]) == 1
