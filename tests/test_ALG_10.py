import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_10 import missing_number

def test_missing_number_basic():
    assert missing_number([3,0,1]) == 2

def test_missing_number_other():
    assert missing_number([0,1]) == 2
