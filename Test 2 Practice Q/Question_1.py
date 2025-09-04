#Asks user to enter an integer n(1-20)
n = int(input("Enter the number of daily temperatures (1-20): "))

#Create an empty list to store temperatures
temperatures = []

#Ask the user to enter n temperatures
for i in range(n):
    temp = int(input("Enter temperature (between -30 and 50): "))
    temperatures.append(temp)

# Calculate average temperature
avg_temp = sum(temperatures) / n

#Find highest and lowest temperatures
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

#Sort temperatures
sorted_temps = sorted(temperatures)

#Print results
print("\nResults:")
print("Average temperature:", avg_temp)
print("Highest temperature:", highest_temp)
print("Lowest temperature:", lowest_temp)
print("Temperatures sorted from lowest to highest:", sorted_temps)