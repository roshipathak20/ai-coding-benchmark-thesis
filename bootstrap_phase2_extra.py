from pathlib import Path
import csv

ROOT = Path(".").resolve()

# Create folders
dirs = [
    "prompts/algorithm",
    "prompts/real_world",
    "solutions",
    "tests",
    "docs",
]
for d in dirs:
    (ROOT / d).mkdir(parents=True, exist_ok=True)

algorithm_tasks = {
    "ALG_1": {
        "title": "Prime Number Check",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function is_prime(n: int) -> bool.

Requirements:
- Return True if n is prime, otherwise False
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_1 import is_prime

def test_prime_true():
    assert is_prime(7) is True

def test_prime_false():
    assert is_prime(8) is False

def test_prime_edge():
    assert is_prime(1) is False
"""
    },
    "ALG_2": {
        "title": "Fibonacci",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function fibonacci(n: int) -> int.

Requirements:
- Return the nth Fibonacci number
- Example: fibonacci(6) == 8
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_2 import fibonacci

def test_fibonacci_basic():
    assert fibonacci(6) == 8

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1
"""
    },
    "ALG_3": {
        "title": "Balanced Parentheses",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function is_balanced(s: str) -> bool.

Requirements:
- Return True if parentheses are balanced
- Example: "(())" -> True, "(()" -> False
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_3 import is_balanced

def test_balanced_true():
    assert is_balanced("(())") is True

def test_balanced_false():
    assert is_balanced("(()") is False

def test_empty():
    assert is_balanced("") is True
"""
    },
    "ALG_4": {
        "title": "Maximum Subarray",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function max_subarray(nums: list[int]) -> int.

Requirements:
- Return the maximum sum of a contiguous subarray
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_4 import max_subarray

def test_max_subarray_basic():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_single():
    assert max_subarray([1]) == 1
"""
    },
    "ALG_5": {
        "title": "Reverse Words",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function reverse_words(text: str) -> str.

Requirements:
- Reverse the order of words
- Example: "hello world" -> "world hello"
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_5 import reverse_words

def test_reverse_words_basic():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_single():
    assert reverse_words("hello") == "hello"
"""
    },
    "ALG_6": {
        "title": "Find Duplicate",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function find_duplicate(nums: list[int]) -> int.

Requirements:
- Return the duplicated number
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_6 import find_duplicate

def test_find_duplicate_basic():
    assert find_duplicate([1,3,4,2,2]) == 2
"""
    },
    "ALG_7": {
        "title": "Merge Intervals",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function merge_intervals(intervals: list[list[int]]) -> list[list[int]].

Requirements:
- Merge overlapping intervals
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_7 import merge_intervals

def test_merge_intervals_basic():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
"""
    },
    "ALG_8": {
        "title": "Longest Word",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function longest_word(words: list[str]) -> str.

Requirements:
- Return the longest word
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_8 import longest_word

def test_longest_word_basic():
    assert longest_word(["cat", "elephant", "dog"]) == "elephant"
"""
    },
    "ALG_9": {
        "title": "Anagram Check",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function is_anagram(a: str, b: str) -> bool.

Requirements:
- Return True if the strings are anagrams
- Ignore spaces and case
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_9 import is_anagram

def test_anagram_true():
    assert is_anagram("listen", "silent") is True

def test_anagram_false():
    assert is_anagram("hello", "world") is False
"""
    },
    "ALG_10": {
        "title": "Missing Number",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a Python function missing_number(nums: list[int]) -> int.

Requirements:
- Return the missing number in range 0..n
- Use type hints
- Include a main() example
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.ALG_10 import missing_number

def test_missing_number_basic():
    assert missing_number([3,0,1]) == 2

def test_missing_number_other():
    assert missing_number([0,1]) == 2
"""
    },
}

real_world_tasks = {
    "RW_1": {
        "title": "Pandas Aggregation",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Using pandas, create a function total_sales_per_product(df) that returns total sales grouped by product.

Requirements:
- Input dataframe has columns: product, amount
- Return a dataframe with total amount per product
- Use type hints if appropriate
- Include a main() example
""",
        "test": """import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_1 import total_sales_per_product

def test_total_sales_per_product():
    df = pd.DataFrame({"product": ["A", "B", "A"], "amount": [10, 20, 5]})
    result = total_sales_per_product(df)
    result_dict = dict(zip(result["product"], result["amount"]))
    assert result_dict == {"A": 15, "B": 20}
"""
    },
    "RW_2": {
        "title": "JSON Username Extraction",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a function extract_usernames(data) that extracts usernames from JSON-like data.

Example input:
{"users":[{"username":"alice"},{"username":"bob"}]}

Expected output:
["alice","bob"]
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_2 import extract_usernames

def test_extract_usernames():
    data = {"users": [{"username": "alice"}, {"username": "bob"}]}
    assert extract_usernames(data) == ["alice", "bob"]
"""
    },
    "RW_3": {
        "title": "Flask Status Endpoint",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Create a Flask app with endpoint /status that returns JSON {"status":"ok"}.
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_3 import app

def test_status_endpoint():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
"""
    },
    "RW_4": {
        "title": "Fetch Titles from API",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a function fetch_titles(url) that uses requests to fetch JSON and returns a list of title fields.
- Raise for bad status
- Use timeout=10
""",
        "test": """import sys
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
"""
    },
    "RW_5": {
        "title": "Top 10 Frequent Words",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a function top_words(file_path) that reads a text file and returns the 10 most frequent words.
- Ignore punctuation
- Ignore case
""",
        "test": """import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_5 import top_words

def test_top_words(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello hello world world world", encoding="utf-8")
    result = top_words(str(file_path))
    assert result[0][0] == "world"
    assert result[0][1] == 3
"""
    },
    "RW_6": {
        "title": "CSV Column Averages",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a function csv_column_averages(file_path) that reads a CSV file and returns average values of numeric columns.
""",
        "test": """import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_6 import csv_column_averages

def test_csv_column_averages(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("a,b\\n1,2\\n3,4\\n", encoding="utf-8")
    result = csv_column_averages(str(file_path))
    assert result == {"a": 2.0, "b": 3.0}
"""
    },
    "RW_7": {
        "title": "Logging Instead of Print",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Modify a divide function so that errors are logged using Python logging instead of print.
""",
        "test": """import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_7 import divide

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_zero():
    assert divide(10, 0) is None
"""
    },
    "RW_8": {
        "title": "Email Validation",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write a function validate_email(email: str) -> bool using regex.
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_8 import validate_email

def test_validate_email_true():
    assert validate_email("test@example.com") is True

def test_validate_email_false():
    assert validate_email("invalid-email") is False
"""
    },
    "RW_9": {
        "title": "SQL Query for Total Purchases",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY SQL, no explanation.

Task: Write an SQL query that returns total purchase amount per customer from:
customers(id, name)
orders(id, customer_id, amount)

Output columns:
customer_name, total_spent
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_9 import query

def test_sql_contains_join_and_sum():
    q = query.lower()
    assert "join" in q
    assert "sum" in q
    assert "group by" in q
"""
    },
    "RW_10": {
        "title": "Pytest Tests for Factorial",
        "prompt": """You are assisting in a controlled AI coding experiment.

Return ONLY Python code.

Task: Write pytest tests for the following function:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
""",
        "test": """import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import solutions.RW_10 as rw10

def test_test_file_has_pytest_tests():
    file_text = open(rw10.__file__, "r", encoding="utf-8").read()
    assert "def test_" in file_text
"""
    },
}

# Write prompt files, tests, and solution placeholders
for key, info in algorithm_tasks.items():
    (ROOT / "prompts" / "algorithm" / f"{key}.txt").write_text(info["prompt"], encoding="utf-8")
    (ROOT / "tests" / f"test_{key}.py").write_text(info["test"], encoding="utf-8")
    (ROOT / "solutions" / f"{key}.py").write_text("# Paste AI-generated code here\n", encoding="utf-8")

for key, info in real_world_tasks.items():
    (ROOT / "prompts" / "real_world" / f"{key}.txt").write_text(info["prompt"], encoding="utf-8")
    (ROOT / "tests" / f"test_{key}.py").write_text(info["test"], encoding="utf-8")
    if key == "RW_9":
        (ROOT / "solutions" / f"{key}.py").write_text('query = """-- Paste AI-generated SQL here"""\\n', encoding="utf-8")
    else:
        (ROOT / "solutions" / f"{key}.py").write_text("# Paste AI-generated code here\n", encoding="utf-8")

# Append rows to results.csv if it exists
results_file = ROOT / "results" / "results.csv"
if results_file.exists():
    existing = results_file.read_text(encoding="utf-8")
    with results_file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for key in algorithm_tasks:
            writer.writerow([key, "algorithmic", "ChatGPT", "", "", "", "", "", ""])
        for key in real_world_tasks:
            writer.writerow([key, "real_world", "ChatGPT", "", "", "", "", "", ""])

# Write benchmark category note
bench_desc = ROOT / "docs" / "benchmark_extension.md"
bench_desc.write_text(
"""# Benchmark Extension

This file documents the additional benchmark tasks added after the initial implementation and maintenance benchmark.

## Added categories
- 10 algorithmic tasks
- 10 real-world development tasks

## Purpose
These tasks expand the benchmark to better reflect:
- algorithmic correctness
- real-world library usage
- backend/API development
- refactoring and practical coding utilities

## Benchmark total
- Initial tasks: 20
- Additional tasks: 20
- Total tasks: 40
""",
    encoding="utf-8"
)

print("Additional benchmark structure created successfully.")