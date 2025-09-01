def is_year_leap(year):
	if year % 4 != 0:       #Can't be divided by 4, not a leap year
		return False
	elif year % 100 != 0:   #Can be divided by 4 but not by 100, is a leap year
		return True
	elif year % 400 != 0:   #Can be divided by 100 but not by 400, not a leap year
		return False
	else:                   #Can be divided by 400, is a leap year
		return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

