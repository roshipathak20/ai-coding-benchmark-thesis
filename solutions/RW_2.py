# Task: Extract usernames from JSON data
# Write a Python function extract_usernames(data)
#
# Example input:
# {"users":[{"username":"alice"},{"username":"bob"}]}
#
# Expected output:
# ["alice","bob"]
#
# The function should loop through the JSON
# and return a list of usernames.

def extract_usernames(data):
    usernames = []
    for user in data.get("users", []):
        if "username" in user:
            usernames.append(user["username"])
    return usernames