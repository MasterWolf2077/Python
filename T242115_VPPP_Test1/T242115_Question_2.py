#User input
bread = float(input("Enter price of bread:"))
milk = float(input("Enter price of milk:"))
chocolate = float(input("Enter price of chocolate:"))

#Subtotal
subtotal = bread + milk + chocolate

#VAT @ 15% calculation
vat = subtotal * 0.15

#Total amount due
total_due = round(subtotal + vat *0.15, 2)

#Output
print("Summary of sales receipt: ")
print("Subtotal: R", subtotal)
print("VAT @ 15%: R", vat)
print("Total amount due: R", round(total_due, 2))