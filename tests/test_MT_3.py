import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_3 import unique_preserve_order

def test_unique_preserve_order():
    assert unique_preserve_order([1, 2, 1, 3, 2]) == [1, 2, 3]
