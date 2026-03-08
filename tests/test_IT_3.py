import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_3 import two_sum

def test_basic_case():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)

def test_other_case():
    assert two_sum([3, 2, 4], 6) == (1, 2)

def test_no_solution():
    assert two_sum([1, 2, 3], 10) is None
