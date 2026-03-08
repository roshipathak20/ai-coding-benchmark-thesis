# Task: Email validation
# Write a Python function validate_email(email: str) -> bool
#
# The function should use regex
# to validate whether the email format is correct.
#
# Example:
# "test@example.com" -> True
# "invalid-email" -> False

import re

def validate_email(email: str) -> bool:
    # Define a regex pattern for validating an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    return re.match(pattern, email) is not None     