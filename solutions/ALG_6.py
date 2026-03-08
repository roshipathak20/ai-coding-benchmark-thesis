# Task: Find duplicate number
# Write a Python function find_duplicate(nums: list[int]) -> int
#
# The list contains numbers where exactly one number
# appears twice.
#
# The function should return that duplicate number.
#
# Example:
# [1,3,4,2,2] -> 2

def find_duplicate(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # This line should never be reached if input is valid