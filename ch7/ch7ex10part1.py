#Matt Hall
#ISY 150
#Chapter 7 Exercise 10
#10/14/2013

#A program that will read each player's name and gold score
#as keyboard input and then save these records in a file
#named 'golf.txt'. (Each record will have a field for the
#player's name and a field for the player's score.)

def main():
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
			else:
				#get input from user
				score = int(input("What did "+ name + " score?\n"))
				#write user input to file
				scorecard_file.write(name + '\t'*2 + str(score) + '\n')
		except ValueError:
			print("ERROR: You shouldn't be able to do this...")
	#close golf.txt file
	scorecard_file.close()
	print("Names and scores have been recorded.")
#execute main function
main()
