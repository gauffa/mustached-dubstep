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

import random

def generate_problem():
	num1 = random.randint(1,999)
	num2 = random.randint(1,999)
	#additional formating is needed to adjust the position of two digit and three digit nubmers
	print('\t' + str(num1))
	print('+\t' + str(num2))
	print('-'*11)
	total = num1 + num2
	return total

def main():
	total = generate_problem()
	user_input = int(input("What is the correct answer? "))
	if user_input == total:
		print("Correct!")
	else:
		print("Incorrect! The correct answer is", str(total) + ".")

main()
