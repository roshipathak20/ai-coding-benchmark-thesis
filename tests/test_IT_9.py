import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_9 import extract_title

def test_extract_title():
    html = "<html><head><title>Test Page</title></head><body></body></html>"
    assert extract_title(html) == "Test Page"

def test_no_title():
    html = "<html><head></head><body></body></html>"
    assert extract_title(html) == ""
