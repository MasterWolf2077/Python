# List of forbidden usernames
forbidden_usernames = ["admin", "root", "test"]

# Ask the user for a username
username = input("Enter a username: ")

# Keep track of how many rules are broken
broken_rules = 0

# Rule 1: Must be at least 5 characters
if len(username) < 5:
    broken_rules += 1

# Rule 2: Must start with a letter
if not username[0].isalpha():  # isalpha() checks if it's a letter
    broken_rules += 1

# Rule 3: Can only contain letters, numbers, or underscores
for char in username:
    if not (char.isalnum() or char == "_"):
        broken_rules += 1
        break  # Stop checking further, no need to count more than once

# Rule 4: Must not be a forbidden username
if username.lower() in forbidden_usernames:
    broken_rules += 1

# Display result
if broken_rules >= 2:
    print("INVALID – The username breaks 2 or more rules.")
elif broken_rules == 1:
    print("VALID (Needs Improvement) – The username breaks 1 rule.")
else:
    print("VALID (Good) – The username passes all rules!")
