def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)): # Check divisors up to the square root of num
        if num % i == 0:    # If num is divisible by i, it's not prime
            return False    
    return True

for i in range(1, 20):  # Check numbers from 1 to 20
    if is_prime(i + 1): # Check if the number is prime
        print(i + 1, end=" ")   
print()
