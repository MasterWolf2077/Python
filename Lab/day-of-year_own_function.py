def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

def day_of_year(year, month, day):	#calculates the day number of the year
	days = 0						#starts at 0
	for m in range(1, month):		#adds the days in each month before the current month
		md = days_in_month(year, m)	#gets the number of days in month m
		if md == None:				#invalid month
			return None
		days += md					#adds the number of days in month m to the total
	md = days_in_month(year, month)	#gets the number of days in the current month
	if day >= 1 and day <= md:		#checks if the day is valid
		return days + day			#adds the days in the current month to the total and returns it
	else:
		return None

print(day_of_year(2000, 12, 31))
