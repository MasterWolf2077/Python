#User input
value = float(input("Enter the value length:"))
unit = input("Enter the unit(m, cm, km):") 

#Conversion
meters = (value / 100 if unit == "cm" else value * 1000 if unit == "km" else value)
centimeters = meters * 100
kilometers = meters / 1000

#Output
print("Meters:", meters)
print("Centimeters:", centimeters)
print("Kilometers:", kilometers)