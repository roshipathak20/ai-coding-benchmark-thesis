import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_5 import merge_sorted_lists

def test_basic_merge():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_one_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]

def test_both_empty():
    assert merge_sorted_lists([], []) == []
