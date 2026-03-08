import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_1 import binary_search

def test_found_middle():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2

def test_found_first():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

def test_found_last():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

def test_not_found():
    assert binary_search([1, 2, 3, 4, 5], 9) == -1

def test_empty():
    assert binary_search([], 1) == -1
