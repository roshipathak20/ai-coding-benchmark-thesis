import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_8 import has_extension

def test_basic_extension():
    assert has_extension("report.PDF", "pdf") is True

def test_multiple_dots():
    assert has_extension("archive.tar.gz", "gz") is True

def test_no_extension():
    assert has_extension("README", "md") is False
