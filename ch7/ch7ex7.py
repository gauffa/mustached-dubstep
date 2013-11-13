#Matt Hall
#ISY 150
#Chapter 7 Exercise 7
#10/14/2013

#Write a program that writes a series of random numbers to a file.
#Each random number should be in the range of 1 through 100.
#The application should let the user specify how many random numbers
#the file will hold.
import random

def main():
	#take user input
	count = int(input("Please enter the amount of numbers to generate:\n"))
	#open file to hold output
	random_number_file = open('numbers.txt','w')
	#iterate for loop 'count' number of times
	for x in range(count):
		random_number = random.randint(1,100)
		random_number_file.write(str(random_number)+"\n")
	#close output file
	random_number_file.close()

main()
