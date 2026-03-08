import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_8 import validate_email

def test_validate_email_true():
    assert validate_email("test@example.com") is True

def test_validate_email_false():
    assert validate_email("invalid-email") is False
