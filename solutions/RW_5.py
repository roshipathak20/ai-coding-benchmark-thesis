# Task: Top frequent words in file
# Write a Python function top_words(file_path)
#
# The function should:
# - read a text file
# - count word frequencies
# - return the 10 most frequent words
#
# Ignore case and punctuation.

def top_words(file_path):
    from collections import Counter
    import re

    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        return word_counts.most_common(10)  