#Passowrd Strength Checker Meter

#Ask user for a password
password = input("Enter a password:")

#Track rate rules
rate_rules = 0

#Rule 1: At least 8 characters
if len(password) >= 8:
    rate_rules += 1

#Rule 2: Include both uppercase and lowercase letters
for char in password:
    if char.islower():
        for char in password:
            if char.isupper():
                rate_rules += 1
                break
        break

#Rule 3: Contains at least one number
if any(char.isdigit() for char in password):
    rate_rules += 1

#Rule 4: Contains at least one special symbol
if any(not char.isalnum() for char in password):
    rate_rules += 1

#Display results
if rate_rules == 4:
    print("Password strength: STRONG")
elif rate_rules == 3:
    print("Password strength: MEDIUM")
else:
    print("Password strength: WEAK")