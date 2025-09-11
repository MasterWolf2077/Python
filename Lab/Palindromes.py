text = input("Enter a text: ")

#Remove spaces
text = text.replace(" ", " ")

#Checking if word is the same in reverse
if len(text) > 1 and text.upper() == text[::-1].upper():
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")