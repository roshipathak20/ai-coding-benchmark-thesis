# Task: Balanced parentheses
# Write a Python function is_balanced(s: str) -> bool
#
# The function should return True if the parentheses in the string
# are balanced and False otherwise.
#
# Balanced examples:
# "(())" -> True
# "()()" -> True
#
# Unbalanced examples:
# "(()" -> False
# "())(" -> False
#
# Only parentheses need to be checked.

def is_balanced(s: str) -> bool:
    stack: list[str] = []
    pairs: dict[str, str] = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0