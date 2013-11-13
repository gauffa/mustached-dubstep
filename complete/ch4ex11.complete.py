########
#Matthew Hall
#Chapter 4
#Exercise 11
#Create: 09/22/2013
#Last Changed: 09/25/2013
########

def main():
	print("This script converts seconds to other units of measurement",\
		"if the number of seconds is greater than 60.\n")
	#get input from user
	seconds = float(input("Enter a number of seconds, please.\n"))
	#math the input
	if seconds > 60 and seconds < 3600:
		amount = seconds / 60
		unit = "minute(s)"
	elif seconds > 3600 and seconds < 86400:
		amount = seconds / 3600
		unit = "hour(s)"
	elif seconds > 86400:
		amount = seconds / 86400
		unit = "day(s)"
	else:
		amount = seconds
		unit = "second(s)"
	#print output
	print("\nThe number of seconds you entered (" + \
		format(float(seconds),'.2f') + ") equals", \
		format(float(amount),'.2f'), unit + ".")
	
main()
