import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_8 import longest_word

def test_longest_word_basic():
    assert longest_word(["cat", "elephant", "dog"]) == "elephant"
