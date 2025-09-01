def is_year_leap(year):
	if year % 4 != 0:       #Can't be divided by 4, not a leap year
		return False
	elif year % 100 != 0:   #Can be divided by 4 but not by 100, is a leap year
		return True
	elif year % 400 != 0:   #Can be divided by 100 but not by 400, not a leap year
		return False
	else:                   #Can be divided by 400, is a leap year
		return True


def days_in_month(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]  #Gets the days from the list
	if month == 2 and is_year_leap(year):
		res = 29    # Adjust for the leap years
	return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr,mo,"-> ",end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
