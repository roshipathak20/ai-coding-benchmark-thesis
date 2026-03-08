import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_7 import search_users

def test_search_case_insensitive():
    users = ["Alice", "bob", "ALINA", "charlie"]
    assert search_users(users, "ali") == ["Alice", "ALINA"]
