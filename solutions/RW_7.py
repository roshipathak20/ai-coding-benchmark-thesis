# Task: Logging errors
# Write a Python function divide(a, b)
#
# The function should divide a by b.
#
# If division by zero occurs:
# - log the error using Python logging
# - return None

import logging

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("Division by zero error: %s", e)
        return None 