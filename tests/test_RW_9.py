import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_9 import query

def test_sql_contains_join_and_sum():
    q = query.lower()
    assert "join" in q
    assert "sum" in q
    assert "group by" in q
