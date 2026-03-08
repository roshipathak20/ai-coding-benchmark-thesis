import sys
import os
from unittest.mock import Mock, patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_7 import fetch_json

def test_fetch_json_success():
    fake_response = Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.json.return_value = {"ok": True}

    with patch("solutions.IT_7.requests.get", return_value=fake_response) as mock_get:
        result = fetch_json("https://example.com/api")
        assert result == {"ok": True}
        mock_get.assert_called_once_with("https://example.com/api", timeout=10)
