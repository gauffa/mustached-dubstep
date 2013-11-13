#Matt Hall
#ISY 150
#Chapter 9 Exercise 5
#10/27/2013

#Write a program that asks the user to enter a 10-character telephone number in
#the format XXX-XXX-XXXX. The program should display the telephone number with any
#alphanetic characters that appeared in the orignal translated to their numeric
#equivalent. For example, if the user enters 555-GET-FOOD the app should display
#555-438-3663.

#ABC = 2, DEF = 3, GHI = 4, JKL = 5, MNO = 6, PQRS = 7, TUV = 8, WXYZ = 9

def user_input():
	input_str = 'Enter your alpha-numeric phone number (ex. XXX-XXX-XXXX):\n'
	ok = False
	while ok == False:
		try:
			input_number = input(input_str)
			if input_number == '':
				print("Blank input received. Program terminated.")
				return
			elif len(input_number) != 12:
				print("Your phone number length is incorrect.")
			elif input_number[3] != '-' or input_number[7] != '-':
				print("Your phone number format is incorrect.")
			elif input_number.isdigit():
				print("Your phone number has no letters.")
			else:	
				ok = True
		except ValueError:
			print('ERROR: You broked it. Please try again.')
	return input_number

def convert_text_to_number(ui_number):
	#declare lists
	alpha_number_list = []
	number_list = []
	conversion_list = ['0','1','2abc','3def','4ghi','5jkl','6mno','7pqrs','8tuv','9wxyz']
	#declare local variables
	phone_numerals = ''
	new_var = ''
	#transfer user input to list
	for x in ui_number:
		alpha_number_list.append(x)
	#iterate through list and check against below
	for x in alpha_number_list:
		for c in conversion_list:
			new_var = conversion_list.index(x)

		

		#append output of each iteration to list
		number_list.append(new_var)

	#put working list into string format
	for x in number_list:
		phone_numerals += x

	return phone_numerals

def output(org_number,new_number):
	print('\n\nThe number you originally entered is:\n'+org_number.upper()+\
		'\nThe numeral-only phone number is:\n'+new_number+'\n\n')

def main():
	ui_number = user_input()
	#this return allows the program to terminate
	#or handoff to a higher-level program
	if not ui_number:
		return
	else:
		phone_numerals = convert_text_to_number(ui_number)
		output(ui_number,phone_numerals)

main()