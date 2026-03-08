# Task: Prime number checker
# Write a Python function is_prime(n: int) -> bool
# The function should return True if n is a prime number
# and False otherwise.
#
# A prime number is a number greater than 1 that has no divisors
# other than 1 and itself.
#
# Examples:
# is_prime(7) -> True
# is_prime(8) -> False
# is_prime(1) -> False
#
# Use type hints and write clean readable Python code.

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True