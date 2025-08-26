#User input
value = float(input("Enter a temperature value: "))
scale = input("Enter scale letter(C, F, K):")

#Conversion
celsius = ((value / 9/5) -32 if scale == "f" else value -273.15 if scale == "k" else value)
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

#Output
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("Kelvin: ", kelvin)