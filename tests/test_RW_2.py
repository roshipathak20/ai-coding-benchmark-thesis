import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_2 import extract_usernames

def test_extract_usernames():
    data = {"users": [{"username": "alice"}, {"username": "bob"}]}
    assert extract_usernames(data) == ["alice", "bob"]
