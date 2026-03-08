# Task: Maximum subarray sum
# Write a Python function max_subarray(nums: list[int]) -> int
#
# The function should return the maximum possible sum
# of a contiguous subarray.
#
# Example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output -> 6
# Because the subarray [4,-1,2,1] has the largest sum.
#
# Use efficient logic and type hints.

def max_subarray(nums: list[int]) -> int:
    max_current = max_global = nums[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current

    return max_global
    