# Task: Reverse words in a sentence
# Write a Python function reverse_words(text: str) -> str
#
# The function should reverse the order of words
# in the given sentence.
#
# Example:
# "hello world" -> "world hello"
#
# Words are separated by spaces.

def reverse_words(text: str) -> str:
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)