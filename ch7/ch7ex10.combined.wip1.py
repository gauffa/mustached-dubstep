def get_name():
	#get input from user
	#upon meeting length requirements ends and returns NAME
	ok = True
	print("\nLeave the line blank and press ENTER to finish entering names and scores.")
	while ok == True:
		try:
			name = str(input("\nWhat is the player's name:\n"))
			ok = name_error_check(name)
			name_space = 16 - len(name)
		except ValueError:
			print("ERROR: Well, shit.")
	return name,name_space

def name_error_check(name):
	if len(name) > 15:
		print("\nThe length of a player name cannot be greater than 15",\
		 "characters.\nPlease try again.\n")
		return True
	else:
		return False

def get_score(name):
	#get input from user
	#loop handles value errors
	ok = True
	while ok == True:
		try:
			score = int(input("What did "+ name + " score?\n"))
			ok = score_error_check(score)
			if len(str(score)) == 1:
				score_space = 4
			else:
				score_space = 3
			if score < 0 and len(str(score)) == 2:
				pass
			elif score < 0:
				score_space -= 1
			else:
				pass
		except ValueError:
			print("ERROR: Dammit.")
	return score,score_space
#upon meeting interger reqs and being between 99 and -99 returns SCORE
def score_error_check(score):
	if score > 99 or score < -99:
		print("\nA score over 99 or below -99 will not be recorded.",\
			"\nPlease try again.\n")
		return True
	else:
		return False
#opens/creates golf.txt for writing
#calls functions to write names/scores to golf.txt
def create_scorecard_loop():
	scorecard_file = open('golf.txt','w')
	ok = True
	while ok == True:
		try:
			name,name_space = get_name()
			if name == '':
				#This false doesn't work before scores are asked for
				#that would be bad
				ok = False
				#break does what I wanted to the false to do
				break
			else:
				pass
			score,score_space = get_score(name)
			write_score(name,name_space,score,score_space,scorecard_file)
		except ValueError:
			print("ERROR: Oh, for the love of...")
	#close golf.txt file
	scorecard_file.close()
	print("Names and scores have been recorded to the scorecard.")	
#opens/creates golf.txt for appending
#calls functions to write names/scores to golf.txt
def append_scorecard_loop():
	scorecard_file = open('golf.txt','a')
	ok = True
	while ok == True:
		try:
			name,name_space = get_name()
			if name == '':
				#This false doesn't work before scores are asked for
				#that would be bad
				ok = False
				#break does what I wanted to the false to do
				break
			else:
				pass
			score,score_space = get_score(name)
			write_score(name,name_space,score,score_space,scorecard_file)
		except ValueError:
			print("ERROR: Oh, for the love of...")
	#close golf.txt file
	scorecard_file.close()
	print("Names and scores have been added to the previous scorecard.")	

#writes variables to golf.txt
def write_score(name,name_space,score,score_space,scorecard_file):
	scorecard_file.write(name+' '*name_space+' '*score_space+str(score)+'\n')

#function that reads the records from the 'golf.txt' file and displays them.
def show_scorecard():
	scorecard_file = open('golf.txt','r')
	#print heading for scorecard_file
	header1 = "Player Name"+"\t"+"Score"
	header2 = (len(header1)+4)*"-"
	print(header1+'\n'+header2)
	for x in scorecard_file:
		line = str(x)
		line = line.rstrip('\n')
		print(line)
	scorecard_file.close()
	print("End of scores"+"\n")

#menu based function that handles other functions for
#creating a new scorecard, adding to the current card,
#displaying the current card and quitting the program.
def main():
	menu_title = "Golf Score Tracker"
	header_line = len(menu_title)*'-'
	new_scorecard_str = "(1) Start a new scorecard"
	append_scorecard_str = "(2) Add scores to the current scorecard"
	display_scorecard_str = "(3) Display current scorecard"
	end_prog_str = "(Q) Quit Program"
	while True:
		try:
			print(menu_title+'\n'+header_line+'\n'+new_scorecard_str+\
				'\n'+append_scorecard_str+'\n'+display_scorecard_str+\
				'\n'+end_prog_str+'\n')
			choice = str(input("Please enter 1, 2, 3 or Q:\n"))
			if str(choice).lower() == "q":
				print("\nProgram terminated.\n")
				break
			elif str(choice) == "1":
				create_scorecard_loop()
			elif str(choice) == "2":
				append_scorecard_loop()
			elif str(choice) == "3":
				show_scorecard()
			else:
				print("\nPlease enter 1, 2, 3 or Q.\n")
		except ValueError:
			print('\nERROR: Please try again.\n')

main()