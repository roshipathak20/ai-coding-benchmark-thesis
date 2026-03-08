# Task: Find missing number
# Write a Python function missing_number(nums: list[int]) -> int
#
# The list contains numbers from 0..n but one number is missing.
#
# Example:
# [3,0,1] -> 2
#
# The function should return the missing number.

def missing_number(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum