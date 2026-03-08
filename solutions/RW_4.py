# Task: Fetch titles from API
# Write a Python function fetch_titles(url)
#
# The function should:
# - use requests.get
# - fetch JSON data from the URL
# - extract the "title" field from each object
# - return a list of titles
#
# Use requests library.

import requests
def fetch_titles(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return [item["title"] for item in data if "title" in item]