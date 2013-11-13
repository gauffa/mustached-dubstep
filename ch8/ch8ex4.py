#Matt Hall
#ISY 150
#Chapter 8 Exercise 4
#10/21/2013

#Design a program that asks the user to enter a series of 20 numbers.
#The program should store the numbers in a list and then display the
#following data:

#The lowest number in the list
#The highest number in the list
#The total of the numbers in the list
#The average of the numbers in the list


def user_input():
	count = 0
	series_list = []
	while count != 20:
		try:
			print("Current entry is "+str(count+1)+" of 20.")
			number = int(input("Please enter a number:\n"))
			count += 1
			series_list.append(number)

		except ValueError:
			print("Numbers! I said numbers! Integers only! Sheesh!")
	return series_list

def list_total(var_list):
	total = 0
	for x in var_list:
		total += x
	return total

def list_average(var_list,total):
	average = 0
	average = total / len(var_list)
	return average

def main():
	series_list = user_input()
	print("The lowest number entered is "+str(min(series_list))+".")
	print("The highest number entered is "+str(max(series_list))+".")
	total = list_total(series_list)
	print("The total sum of all entered numbers is "+str(total)+".")
	average = list_average(series_list,total)
	print("The average of all entered numbers is "+format(average,'.2f')+".")

main()