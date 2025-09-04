import math  # We use this for the square root function

# Ask the user for a number m
m = int(input("Enter a number (1 or more): "))

# List to store perfect squares
perfect_squares = []

# We only need to check numbers up to the square root of m
# For each number n, calculate n*2
for n in range(1, int(math.sqrt(m)) + 1):
    square = n * n
    if square <= m:
        perfect_squares.append(square)

# Print results
print("Perfect squares up to", m, ":")
for sq in perfect_squares:
    print(sq, end=" ")  # Print squares in one line separated by spaces
