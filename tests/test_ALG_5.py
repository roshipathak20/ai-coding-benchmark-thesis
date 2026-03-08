import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_5 import reverse_words

def test_reverse_words_basic():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_single():
    assert reverse_words("hello") == "hello"
