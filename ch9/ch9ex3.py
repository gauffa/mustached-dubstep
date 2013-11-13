#Matt Hall
#ISY 150
#Chapter 9 Exercise 3
#10/27/2013

#Write a program that reads a string from the user containing a date in
#the form mm/dd/yyyy. It should print the date in the form March 12, 2012.

#add input validation to insure months,days,years are valid numbers/positions
#on a calendar

def user_input():
	preinput_str = 'A blank response will terminate the program.'
	input_str = 'Please enter a date in the format of: mm/dd/yyyy\n'
	ok = False
	while ok == False:
		try:
			input_date = input(preinput_str+'\n'+input_str)
			date_list = input_date.split('/')
			#validate input
			if input_date == '':
				print("Blank input recieved. Program terminated.")
				quit()
			elif not (1 <= int(date_list[0]) <= 12):
				print("ERROR: Month must be 1 through 12.")
			elif not (1 <= int(date_list[1]) <= 31):
				print("ERROR: Day must be 1 through 31.")
			elif not (1 <= int(date_list[2]) <= 9999):
				print("ERROR: Year must be 1 through 9999.")
			else:
				print("Input accepted.")
				ok = True
		except ValueError:
			print("ERROR: At least one of the elements of the date is incorect!")
		except KeyboardInterrupt:
			print("ERROR: A blank input can be used to terminate this program.")
		except IndexError:
						print("ERROR: NO! Try again... Please.")
		
	return date_list[1],date_list[0],date_list[2]

def display_output(day,month,year):
	month_list = ['January','February','March','April','May','June',\
					  'July','August','September','October','November',\
					  'December']
	print('Based on the input provided the written date is: '\
		+month_list[int(month)-1]+' '+str(day)+', '+str(year))

def main():
	day,month,year = user_input()
	display_output(day,month,year)
main()
