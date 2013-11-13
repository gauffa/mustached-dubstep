#Matt Hall
#ISY 150
#Chapter 8 Exercise 9
#10/21/2013

#Write a program that lets the user enter the name of a team
#and then dispalys the number of times that team has won the
#World Series in the time period from 1903 and 2009.

def fill_list_for():
	team_wins_file = open('WorldSeriesWinner.txt','r')
	#initialize list
	team_wins_list = []
	#iterate over file object to populate list
	for x in team_wins_file:
		#appends each line from file object and removes '\n'
		team_wins_list.append(x.rstrip('\n'))
	team_wins_file.close()
	#return list to calling function
	return team_wins_list

def list_each_team_once(teams):
	list_each_team_once_working_list = []
	
	for x in teams:
		list_each_team_once_working_list.append(x)

	sorted_team_list = []		
	while len(list_each_team_once_working_list) != 0:
		try:
			team_check = list_each_team_once_working_list[0]
			if team_check in sorted_team_list:
				del list_each_team_once_working_list[0]
			else:
				sorted_team_list.append(team_check)
		except ValueError:
			print("ERROR:Value Error... What?")
	sorted_team_list.sort()
	return sorted_team_list

def choose_team(teams):
	choose_team_working_list = []
	for x in teams:
		choose_team_working_list.append(x)
	
	for x in choose_team_working_list:
		indx = choose_team_working_list.index(x)
		number = indx + 1
		print(str(number) + '\t' + choose_team_working_list[indx])
	
	ok = False
	while ok == False:
		try:
			choice = int(input("\nA 0 response will terminate the program.\n"))			
			if choice == 0:
				print("0 input received. Program terminated.")
				quit()
			elif 1 <= choice and choice <= 28:
				team_query = choose_team_working_list[choice-1]
				ok = True
			else:
				print("Please choose between 1 and 28.")
		except ValueError as detail:
			print("ERROR: Please choose a number. Between 1 and 28 would be helpful.\n")
	return team_query

def program_purpose():
	print("\nThis program will tell you how many times a team won the world series"+\
		" between\n1903 and 2009. Choose a number between 1 and 28 to select a team.\n")

def user_query(teams):
	#import list for this functions use
	user_query_working_list = []
	for x in teams:
		user_query_working_list.append(x)

	sorted_team_list = list_each_team_once(user_query_working_list)

	#get input from user
	team_query = choose_team(sorted_team_list)

	ok = True
	count = 0
	while ok == True:
		try:
			team_index = user_query_working_list.index(team_query)
			count += 1
			del user_query_working_list[team_index]
		except ValueError:
			return team_query,count
			ok = False

def output(query,count):
	if count == 1:
		time = 'time'
	elif count > 1:
		time = 'times'
	print("The "+query+" won the World Series "+str(count)+\
		" "+time+" bewtween 1903 and 2009.")

def main():
	#call function that populates list and returns list to main
	team_ws_list = fill_list_for()
	program_purpose()
	team_query,count = user_query(team_ws_list)
	output(team_query,count)

main()