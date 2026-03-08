from pathlib import Path
import csv
import textwrap

ROOT = Path(".").resolve()

dirs = [
    "tasks",
    "prompts/implementation",
    "prompts/maintenance",
    "ai_outputs",
    "solutions",
    "tests",
    "screenshots",
    "results",
    "maintenance_sources",
]
for d in dirs:
    (ROOT / d).mkdir(parents=True, exist_ok=True)

(ROOT / "solutions" / "__init__.py").write_text("", encoding="utf-8")

implementation_tasks = {
    "IT_1": {
        "title": "Binary Search",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Implement binary search.

Requirements:
- Function name: binary_search(arr, target)
- Input: sorted list of integers
- Return the index if target is found
- Return -1 if target is not found
- Do not use built-in search methods
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_1 import binary_search

def test_found_middle():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2

def test_found_first():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

def test_found_last():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

def test_not_found():
    assert binary_search([1, 2, 3, 4, 5], 9) == -1

def test_empty():
    assert binary_search([], 1) == -1
"""
    },
    "IT_2": {
        "title": "Palindrome Check",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Determine if a string is a palindrome.

Requirements:
- Function name: is_palindrome(text)
- Ignore spaces and capitalization
- Return True or False
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_2 import is_palindrome

def test_simple_true():
    assert is_palindrome("madam") is True

def test_case_and_space():
    assert is_palindrome("Never Odd Or Even") is True

def test_false():
    assert is_palindrome("hello") is False

def test_empty():
    assert is_palindrome("") is True
"""
    },
    "IT_3": {
        "title": "Two Sum",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Solve the Two Sum problem.

Requirements:
- Function name: two_sum(nums, target)
- Return a tuple of indices of the two numbers that add up to target
- Return None if no solution exists
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_3 import two_sum

def test_basic_case():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)

def test_other_case():
    assert two_sum([3, 2, 4], 6) == (1, 2)

def test_no_solution():
    assert two_sum([1, 2, 3], 10) is None
"""
    },
    "IT_4": {
        "title": "Word Frequency",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Count word frequencies in a sentence.

Requirements:
- Function name: word_frequency(text)
- Ignore capitalization
- Split on whitespace
- Return a dictionary
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_4 import word_frequency

def test_basic_frequency():
    assert word_frequency("apple banana apple") == {"apple": 2, "banana": 1}

def test_case_insensitive():
    assert word_frequency("Hello hello") == {"hello": 2}

def test_empty():
    assert word_frequency("") == {}
"""
    },
    "IT_5": {
        "title": "Merge Sorted Lists",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Merge two sorted lists.

Requirements:
- Function name: merge_sorted_lists(a, b)
- Return a new sorted list
- Do not use sort() on the final combined list
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_5 import merge_sorted_lists

def test_basic_merge():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_one_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]

def test_both_empty():
    assert merge_sorted_lists([], []) == []
"""
    },
    "IT_6": {
        "title": "CSV Average with pandas",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Read a CSV file and compute the average of a numeric column using pandas.

Requirements:
- Function name: csv_average(file_path, column_name)
- Return the mean as float
- Raise ValueError if the column does not exist
- Use pandas
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_6 import csv_average

def test_csv_average_basic(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("name,score\\nA,10\\nB,20\\nC,30\\n", encoding="utf-8")
    assert csv_average(str(file_path), "score") == 20.0

def test_missing_column(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("name,score\\nA,10\\n", encoding="utf-8")
    try:
        csv_average(str(file_path), "age")
        assert False
    except ValueError:
        assert True
"""
    },
    "IT_7": {
        "title": "Fetch JSON using requests",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fetch JSON data from a URL using requests.

Requirements:
- Function name: fetch_json(url)
- Use requests.get
- Return the parsed JSON object
- Raise for bad HTTP status
- Use type hints
- Include a main() example
""",
        "test": """import sys
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
"""
    },
    "IT_8": {
        "title": "JSON Roundtrip",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a dictionary to JSON and read it back.

Requirements:
- Function name: json_roundtrip(file_path, data)
- Write the dictionary to the file
- Read it back and return the loaded dictionary
- Use the json module
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_8 import json_roundtrip

def test_json_roundtrip(tmp_path):
    file_path = tmp_path / "sample.json"
    data = {"name": "Roshi", "age": 25}
    assert json_roundtrip(str(file_path), data) == data
"""
    },
    "IT_9": {
        "title": "HTML Title Parser",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Extract the title from an HTML string using BeautifulSoup.

Requirements:
- Function name: extract_title(html)
- Return the title text as a string
- Return an empty string if no title exists
- Use bs4.BeautifulSoup
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_9 import extract_title

def test_extract_title():
    html = "<html><head><title>Test Page</title></head><body></body></html>"
    assert extract_title(html) == "Test Page"

def test_no_title():
    html = "<html><head></head><body></body></html>"
    assert extract_title(html) == ""
"""
    },
    "IT_10": {
        "title": "Matplotlib Line Plot",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Create a simple line plot and save it to a file using matplotlib.

Requirements:
- Function name: save_line_plot(values, output_path)
- Create a line plot from the values
- Save the figure to output_path
- Close the figure after saving
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_10 import save_line_plot

def test_save_line_plot(tmp_path):
    output_file = tmp_path / "plot.png"
    save_line_plot([1, 3, 2, 5], str(output_file))
    assert output_file.exists()
    assert output_file.stat().st_size > 0
"""
    },
}

maintenance_tasks = {
    "MT_1": {
        "title": "Fix divide-by-zero handling",
        "source": """def safe_divide(a, b):
    return a / b
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: safe_divide(a, b)
- Return None when b is zero
- Otherwise return the division result
- Use type hints
- Include a main() example

Broken code:
def safe_divide(a, b):
    return a / b
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_1 import safe_divide

def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5

def test_safe_divide_zero():
    assert safe_divide(10, 0) is None
"""
    },
    "MT_2": {
        "title": "Fix even-number logic",
        "source": """def is_even(n):
    if n % 2 == 1:
        return True
    return False
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: is_even(n)
- Return True only for even numbers
- Use type hints
- Include a main() example

Broken code:
def is_even(n):
    if n % 2 == 1:
        return True
    return False
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_2 import is_even

def test_even_true():
    assert is_even(4) is True

def test_even_false():
    assert is_even(5) is False
"""
    },
    "MT_3": {
        "title": "Fix duplicate removal preserving order",
        "source": """def unique_preserve_order(items):
    return list(set(items))
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: unique_preserve_order(items)
- Remove duplicates while preserving original order
- Use type hints
- Include a main() example

Broken code:
def unique_preserve_order(items):
    return list(set(items))
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_3 import unique_preserve_order

def test_unique_preserve_order():
    assert unique_preserve_order([1, 2, 1, 3, 2]) == [1, 2, 3]
"""
    },
    "MT_4": {
        "title": "Fix average for empty list",
        "source": """def average(values):
    return sum(values) / len(values)
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: average(values)
- Return 0 for an empty list
- Otherwise return the average
- Use type hints
- Include a main() example

Broken code:
def average(values):
    return sum(values) / len(values)
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_4 import average

def test_average_basic():
    assert average([10, 20, 30]) == 20

def test_average_empty():
    assert average([]) == 0
"""
    },
    "MT_5": {
        "title": "Fix factorial negative input handling",
        "source": """def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: factorial(n)
- Raise ValueError for negative input
- Return 1 for 0
- Use type hints
- Include a main() example

Broken code:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
""",
        "test": """import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_5 import factorial

def test_factorial_basic():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)
"""
    },
    "MT_6": {
        "title": "Fix integer list parser",
        "source": """def parse_int_list(text):
    return [int(x) for x in text.split(",")]
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: parse_int_list(text)
- Input is a comma-separated string
- Ignore invalid items and surrounding spaces
- Return a list of integers
- Use type hints
- Include a main() example

Broken code:
def parse_int_list(text):
    return [int(x) for x in text.split(",")]
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_6 import parse_int_list

def test_parse_valid_and_invalid():
    assert parse_int_list("1, 2, x, 3") == [1, 2, 3]

def test_parse_empty():
    assert parse_int_list("") == []
"""
    },
    "MT_7": {
        "title": "Fix case-insensitive user search",
        "source": """def search_users(users, query):
    return [u for u in users if query in u]
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: search_users(users, query)
- Perform case-insensitive substring matching
- Return matching usernames
- Use type hints
- Include a main() example

Broken code:
def search_users(users, query):
    return [u for u in users if query in u]
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_7 import search_users

def test_search_case_insensitive():
    users = ["Alice", "bob", "ALINA", "charlie"]
    assert search_users(users, "ali") == ["Alice", "ALINA"]
"""
    },
    "MT_8": {
        "title": "Fix file extension validator",
        "source": """def has_extension(filename, extension):
    return filename.split(".")[1] == extension
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: has_extension(filename, extension)
- Support filenames with multiple dots
- Return False if there is no extension
- Comparison should be case-insensitive
- Use type hints
- Include a main() example

Broken code:
def has_extension(filename, extension):
    return filename.split(".")[1] == extension
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_8 import has_extension

def test_basic_extension():
    assert has_extension("report.PDF", "pdf") is True

def test_multiple_dots():
    assert has_extension("archive.tar.gz", "gz") is True

def test_no_extension():
    assert has_extension("README", "md") is False
"""
    },
    "MT_9": {
        "title": "Fix sort by age",
        "source": """def sort_by_age(records):
    return sorted(records, key=lambda x: x["name"])
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: sort_by_age(records)
- Sort ascending by the 'age' field
- Return a new sorted list
- Use type hints
- Include a main() example

Broken code:
def sort_by_age(records):
    return sorted(records, key=lambda x: x["name"])
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_9 import sort_by_age

def test_sort_by_age():
    records = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
    assert sort_by_age(records) == [{"name": "B", "age": 20}, {"name": "A", "age": 30}]
"""
    },
    "MT_10": {
        "title": "Fix range summation",
        "source": """def sum_range(n):
    total = 0
    for i in range(n):
        total += i
    return total
""",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Fix the broken function shown below.

Requirements:
- Keep function name: sum_range(n)
- Return the sum from 1 to n inclusive
- Return 0 for n <= 0
- Use type hints
- Include a main() example

Broken code:
def sum_range(n):
    total = 0
    for i in range(n):
        total += i
    return total
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.MT_10 import sum_range

def test_sum_range_basic():
    assert sum_range(5) == 15

def test_sum_range_zero():
    assert sum_range(0) == 0
"""
    },
}

tasks_md = ["# Phase 2 Benchmark Tasks", "", "## Implementation Tasks", ""]
for key, info in implementation_tasks.items():
    tasks_md.append(f"- {key}: {info['title']}")
tasks_md += ["", "## Maintenance Tasks", ""]
for key, info in maintenance_tasks.items():
    tasks_md.append(f"- {key}: {info['title']}")
(ROOT / "tasks" / "phase2_tasks.md").write_text("\n".join(tasks_md), encoding="utf-8")

for key, info in implementation_tasks.items():
    (ROOT / "prompts" / "implementation" / f"{key}.txt").write_text(info["prompt"], encoding="utf-8")
    (ROOT / "tests" / f"test_{key}.py").write_text(info["test"], encoding="utf-8")
    (ROOT / "solutions" / f"{key}.py").write_text("# Paste AI-generated code here\n", encoding="utf-8")
    (ROOT / "ai_outputs" / f"{key}_attempt1.txt").write_text("", encoding="utf-8")

for key, info in maintenance_tasks.items():
    (ROOT / "prompts" / "maintenance" / f"{key}.txt").write_text(info["prompt"], encoding="utf-8")
    (ROOT / "maintenance_sources" / f"{key}_broken.py").write_text(info["source"], encoding="utf-8")
    (ROOT / "tests" / f"test_{key}.py").write_text(info["test"], encoding="utf-8")
    (ROOT / "solutions" / f"{key}.py").write_text("# Paste AI-generated fixed code here\n", encoding="utf-8")
    (ROOT / "ai_outputs" / f"{key}_attempt1.txt").write_text("", encoding="utf-8")

results_file = ROOT / "results" / "results.csv"
with results_file.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "TaskID", "Category", "Tool", "Attempts", "TimeSeconds", "Pass",
        "Hallucination", "CodeQuality", "Notes", "PromptScreenshot",
        "CodeScreenshot", "TestScreenshot"
    ])
    for key in implementation_tasks:
        writer.writerow([key, "Implementation", "ChatGPT", "", "", "", "", "", "", "", "", ""])
    for key in maintenance_tasks:
        writer.writerow([key, "Maintenance", "ChatGPT", "", "", "", "", "", "", "", "", ""])

readme = """# AI Coding Benchmark Thesis

This repository contains the Phase 2 experiment benchmark for evaluating AI-assisted software development.

## Categories
- 10 implementation tasks
- 10 maintenance tasks

## Workflow per task
1. Open the prompt file
2. Paste the prompt into ChatGPT
3. Save the raw AI response in ai_outputs/
4. Paste the generated code into solutions/
5. Run the corresponding pytest file
6. Take screenshots
7. Record the result in results/results.csv

## Screenshot policy
For each task, save:
- one screenshot of prompt/AI answer
- one screenshot of code in VS Code
- one screenshot of pytest result

## Main command
pytest tests/test_IT_1.py -q
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("Phase 2 experiment structure created successfully.")