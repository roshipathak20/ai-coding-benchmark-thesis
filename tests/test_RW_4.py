import sys
import os
from unittest.mock import Mock, patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_4 import fetch_titles

def test_fetch_titles():
    fake_response = Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = [{"title": "A"}, {"title": "B"}]

    with patch("solutions.RW_4.requests.get", return_value=fake_response):
        assert fetch_titles("https://example.com") == ["A", "B"]
