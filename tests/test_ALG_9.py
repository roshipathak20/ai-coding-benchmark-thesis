import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_9 import is_anagram

def test_anagram_true():
    assert is_anagram("listen", "silent") is True

def test_anagram_false():
    assert is_anagram("hello", "world") is False
