#Matthew Hall
#ISY 150
#Chapter 6 Exercise 2
#10/07/2013
#Math Quiz

#Write a program that gives simple math quizzes.
#The program should display two random numbers
#that are to be added, such as:
#
#	247
#+	129
#
#The program should all the student to enter the
#answer. If answer is correcet, a message of
#congratulations should be displayed. If the
#answer is incorrect, the correct answer should
#be displayed.

##Just for giggles make sure you exit the program using CTRL-C, as least once.


import random
import time
import os

#determines number of spaces needed to line-up output properly
def length_space(var):
	if len(str(var)) == 3:
		spc = 0
	elif len(str(var)) == 2:
		spc = 1
	elif len(str(var)) == 1:
		spc = 2
	return spc

#generates random numbers and displays them formatted properly
def generate_problem():
	num1 = random.randint(1,999)
	num2 = random.randint(1,999)
#uses length_space to determine propering spacing for each number in the print statement
	spc1 = length_space(num1)
	spc2 = length_space(num2)
#sets variables to pass back to main()
	line1 = '\t' + " " * spc1 + str(num1)
	line2 =  '+\t' + " " * spc2 + str(num2)
	line3 = '-'*11
#displays problem
	print(line1 + "\n" + line2 + "\n" + line3)
	total = num1 + num2
#returns each line of the math problem and the correct total to main
	return line1,line2,line3,total

#handles user input
def main():
	line1,line2,line3,total = generate_problem()
#little input validation to keep script from bombing out when invalid input is used.
	while True:
		try:
			user_input = int(input("\nWhat is the correct answer? (CTRL-C to end)\n"))
			if user_input == total:
				print("\nCORRECT!\n", monty_python_quotes() + "\n")
				#break
				main()
			else:
				print("\nINCORRECT! The correct answer is", str(total) + ".\n", monty_python_quotes() + "\n")
				#break
				main()
		except ValueError:
			print("\nERROR: Personally, I blame you. Try an integer next time.\n", monty_python_quotes() + "\n")
			print(line1 + "\n" + line2 + "\n" + line3)
		except KeyboardInterrupt:
			print("\nOff to the pub, eh? Fair enough lemme see if I kin find the switch...\n")
			time.sleep(3)
			print("\nOh! There it is!\n")
			time.sleep(3)
			clear()
			time.sleep(3)
			print("\n\n\n\n\n" + monty_python_quotes() + "\n\n\n\n\n")
			quit()

#just for fun
def monty_python_quotes():
	quote1 = "Listen, strange women lyin' in ponds distributin' swords is no basis for a system of government."
	quote2 = "Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."
	quote3 = "Come and see the violence inherent in the system. Help! Help! I'm being repressed!"
	quote4 = "It's just a flesh wound."
	quote5 = "Bravely taking to his feet, he beat a very brave retreat. A brave retreat by brave Sir Robin."
	quote6 = "It's not a question of where he grips it! It's a simple question of weight ratios! A five ounce bird could not carry a one pound coconut."
	quote7 = "Oh, but you can't expect to wield supreme executive power just because some watery tart threw a sword at you."
	quote8 = "On second thought, let's not go to Camelot. It is a silly place."
	quote9 = "Four shalt thou not count, neither count thou two, excepting that thou then proceed to three."
	quote10 = "There are some who call me... Tim."
	#picks a number between 1 and 10
	number = random.randint(1,10)
	#begins to build quote string with new line and single quote
	quote = "\n'"
	#picks a quote based on random number and adds to 'quote' variable
	if number == 1:
		quote += quote1
	elif number == 2:
		quote += quote2
	elif number == 3:
		quote += quote3
	elif number == 4:
		quote += quote4
	elif number == 5:
		quote += quote5
	elif number == 6:
		quote += quote6
	elif number == 7:
		quote += quote7
	elif number == 8:
		quote += quote8
	elif number == 9:
		quote += quote9
	elif number == 10:
		quote += quote10
	#complete 'quote' variable
	quote += "'\n\t--Monty Python"
	#returns completed quote
	return quote

#this SHOULD clear the screen on most linux distros and Windows
#tested this earlier in IDLE and didn't perform as expected
#it does seem to work from a terminal window, however.
def clear():
	os.system('cls' if os.name=='nt' else 'clear')

main()