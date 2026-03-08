import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_2 import is_palindrome

def test_simple_true():
    assert is_palindrome("madam") is True

def test_case_and_space():
    assert is_palindrome("Never Odd Or Even") is True

def test_false():
    assert is_palindrome("hello") is False

def test_empty():
    assert is_palindrome("") is True
