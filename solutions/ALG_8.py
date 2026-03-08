# Task: Find longest word
# Write a Python function longest_word(words: list[str]) -> str
#
# The function should return the longest word
# in the list.
#
# Example:
# ["cat", "elephant", "dog"] -> "elephant"

def longest_word(words: list[str]) -> str:
    if not words:
        return ""

    longest = words[0]

    for word in words[1:]:
        if len(word) > len(longest):
            longest = word

    return longest