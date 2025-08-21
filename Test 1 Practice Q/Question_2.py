#User input
transport = float(input("Enter trasport cost: "))  # input transport cost
accommodation = float(input("Enter accommodation cost: "))  # input accommodation cost
meals = float(input("Enter meals cost: "))  # input meals cost

#Calculate subtotal of all expenses
subtotal = transport + accommodation + meals

#Calculate service fee @10%
service_fee = subtotal * 0.10

#Final total due (rounded to two decimals)
total_due = round(subtotal + service_fee * 0.10, 2)

#Output
print("Summary of expenses:")
print("Subtotal:", subtotal)
print("Service fee (10%):", service_fee)
print("Final total due:", round(total_due, 2))