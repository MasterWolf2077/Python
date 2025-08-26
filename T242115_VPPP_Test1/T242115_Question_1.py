#User input
hours = int(input("Enter number of hours:"))
minutes = int(input("Enter number of minutes:"))

#Account for negative numbers
if hours < 0 or minutes < 0:
    print("Invalid. Enter non-negative numbers only.")
else:
    #Calculate total number of seconds
    total_seconds = (hours *3600) + (minutes * 60)
    #Output
    print("Total number of seconds: ", total_seconds)