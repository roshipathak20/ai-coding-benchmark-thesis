# Task: Check if two strings are anagrams
# Write a Python function is_anagram(a: str, b: str) -> bool
#
# Two strings are anagrams if they contain
# the same characters in different order.
#
# Example:
# "listen" and "silent" -> True
# "hello" and "world" -> False
#
# Ignore spaces and case differences.

def is_anagram(a: str, b: str) -> bool:
    # Remove spaces and convert to lowercase
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()

    # Sort the characters of both strings and compare
    return sorted(a) == sorted(b)