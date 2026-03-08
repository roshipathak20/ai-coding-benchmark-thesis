import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_6 import find_duplicate

def test_find_duplicate_basic():
    assert find_duplicate([1,3,4,2,2]) == 2
