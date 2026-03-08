import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_4 import average

def test_average_basic():
    assert average([10, 20, 30]) == 20

def test_average_empty():
    assert average([]) == 0
