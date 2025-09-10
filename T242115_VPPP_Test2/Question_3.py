#Prime Number Finder

import math

#Ask user ot enter a number m(must be 2 or more)
m = int(input("Enter a number(2 or more): "))

#Create a list of prime numbers
prime_numbers = []

#Find prime number up to m and only check for factors up to the square root of m, skipping even numbers after 2
for num in range(2, m + 1):
    if num == 2:
        prime_numbers.append(num)
    elif num > 2 and num % 2 != 0:
        is_prime = True
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

#Print the list of prime numbers
print("Prime number up to", m, "are:", prime_numbers)