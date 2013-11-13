#Matt Hall
#ISY 150
#Chapter 7 Exercise 6
#10/14/2013

#Assume that a file containing a series of integers is named numbers.txt
#and exists on the computer's disk. Write a program that calulates the 
#average of all the numbers stored in the file.

#for the sake of testing you can use exercise 7 to generate
#a file that will provide numbers to average

def main():
	total = 0.0
	count = 0
	#open file with numbers to be averaged
	#assign to variable
	random_numbers_file = open('numbers.txt','r')
	#iterate for loop for all lines in 'file'
	for line in random_numbers_file:
		number = float(line)
		count += 1
		total += number
	average = total / count
	print("The average of all the numbers found in 'numbers.txt' is:", format(average,'.2f'))

main()
