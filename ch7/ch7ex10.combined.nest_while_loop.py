#Matt Hall
#ISY 150
#Chapter 7 Exercise 10
#10/14/2013

#A function that will read each player's name and gold score
#as keyboard input and then save these records in a file
#named 'golf.txt'. (Each record will have a field for the
#player's name and a field for the player's score.)
def get_score():
	#open or create golf.txt for writing
	scorecard_file = open('golf.txt','w')
	while True:
		try:
			print("Press ENTER to finish entering names and scores.")
			#get input from user
			name = str(input("What is the player's name:\n"))
			#if the user returns no input end the loop
			if name == '':
				break
			elif len(name) > 15:
				print("\nThe length of a player name cannot be greater than 15",\
				 "characters.\nPlease try again.\n")
			#name length of 15 needs 1 space to line up a 2 digit score
			#name+spc should add up to 16 characters no matter what
			else:
				name_space = 16 - len(name)
				#get input from user
				while True:
					try:
						score = int(input("What did "+ name + " score?\n"))
						if score > 99 or score < -99:
							print("A golf score over 99 or below -99 will not be evaluated.",\
								"\nPlease try again.")
						else:
							pass

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

						#write user input to file
						scorecard_file.write(name+' '*name_space+' '*score_space+str(score)+'\n')
					except ValueError:
						print("ERROR: You broke it.")


				#close golf.txt file
				scorecard_file.close()
				print("Names and scores have been recorded.")

#function that reads the records from the 'golf.txt' file and displays them.
def show_score():
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
	print("\n\n"+"End of scores"+"\n\n")

#menu based function that allows you to take scores then display them.
def main():
	menu_title = "Golf Score Tracker"
	header_line = len(menu_title)*'-'
	input_score_str = "(1) Input Scores"
	display_score_str = "(2) Display Scores"
	end_prog_str = "(Q) Quit Program"
	while True:
		try:
			print(menu_title+'\n'+header_line+'\n\n'+input_score_str+\
				'\n'+display_score_str+'\n'+end_prog_str+'\n')
			choice = str(input("Please enter 1, 2, or Q:\n"))
			if len(choice) == "1":
				print("Please only enter one character.")
			elif str(choice).lower() == "q":
				print("Program terminated.")
				break
			elif str(choice) == "1":
				get_score()
			elif str(choice) == "2":
				show_score()
			else:
				print("Please enter 1, 2 or Q.")
		except ValueError:
			print('ERROR: Please try again.')

main()
