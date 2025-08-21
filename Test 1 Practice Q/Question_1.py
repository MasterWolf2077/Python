#User input for days and hours
days = int(input("Number of days:"))
hours = int(input("Number of hours:"))

#Account for negative numbers
if days < 0 or hours < 0:
    print("Invalid input. Days and hours must be non-negative.")
else:
    #Calculate total number of minutes
    total_minutes = (days * 24 + hours) * 60
    print("Total Minutes:", total_minutes)