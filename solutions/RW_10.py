# Task: Generate pytest tests
#
# Write pytest tests for the following function:
#
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
# Create multiple tests using pytest.
import pytest

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120      