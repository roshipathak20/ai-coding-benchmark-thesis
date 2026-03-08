import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_1 import is_prime

def test_prime_true():
    assert is_prime(7) is True

def test_prime_false():
    assert is_prime(8) is False

def test_prime_edge():
    assert is_prime(1) is False
