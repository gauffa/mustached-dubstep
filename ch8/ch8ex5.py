#Matt Hall
#ISY 150
#Chapter 8 Exercise 5
#10/21/2013

#Write a program that reads the contents of the file into a list.
#Program should then ask the user to enter a charge account number.
#The program should determine whether the number is vaild by searching
#for it in the list. If the number is in the list, the program should
#display a message indicating the number is valid. If the number is
#not in the list, the program should display a message indicating the
#number is not valid.

def read_accounts_file(file_name):
	accounts_list = []
	accounts_file = open(file_name,'r')
	for x in accounts_file:
		accounts_list.append(x.rstrip('\n'))
	return accounts_list

def user_query(accounts_list):
	user_query_list = []
	for x in accounts_list:
		user_query_list.append(x)

	ok = False
	while ok == False:
		try:
			print("A zero '0' will terminate the program.")
			query = int(input("Please enter an account number.\n"))
			if str(query) == '0':
				print("Blank entry received. Program terminated.")
				ok = True
				quit()
			elif str(query) not in user_query_list:
				output_str = 'Account #'+str(query)+' is not present in our database.'
				ok = True
			elif str(query) in user_query_list:
				output_str = 'Account #'+str(query)+' is present in our database.' 
				ok = True
			
		except ValueError:
			print("\nNumbers! I said numbers! Integers!\n")

	return output_str

def main():
	accounts_list = read_accounts_file('charge_accounts.txt')
	output_str = user_query(accounts_list)
	print(output_str)

main()