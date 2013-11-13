##########
#Matt Hall
#Chapter 4 Exercise 11
#09/25/2013
#
##########




def main():
	#get input from user
	seconds = float(input("Enter a number of seconds, please.\n"))
	#math input to determine days, hours, minutes, seconds remainders
	days = seconds//86400
	seconds -= days*86400
	hours = seconds//3600
	seconds -= hours*3600
	minutes = seconds//60
	seconds -= seconds
	#print("Days", days,"Hours",hours,"Minutes",minutes,"Seconds",seconds)

		#format and display output to user
	time = "The caculated time is "
	if days:
		if days > 1:
			time += str(days) + " days "
		else:
			time += str(days) + " day "
	if hours:
		if hours > 1:
			time += str(hours) + " hours "
		else:
			time += str(hours) + " hour "
	if minutes:
		if minutes > 1:
			time += str(minutes) + " minutes "
		else:
			time += str(minutes) + " minute "
	if seconds:
		if seconds > 1:
			time += str(seconds) + " seconds "
		else:
			time += str(seconds) + " second "
	#print concatenated string
	print(time)

main()
