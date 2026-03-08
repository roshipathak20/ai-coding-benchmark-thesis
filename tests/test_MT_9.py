import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_9 import sort_by_age

def test_sort_by_age():
    records = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
    assert sort_by_age(records) == [{"name": "B", "age": 20}, {"name": "A", "age": 30}]
