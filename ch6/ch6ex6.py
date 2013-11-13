#Matthew Hall
#ISY 150
#Chapter 6 Exercise 6
#10/07/2013
#Test Average and Grade

#This function should accept five test scores
#as arguments and return the average of the scores
def calc_average(ts1,ts2,ts3,ts4,ts5):
	ts_avg = (ts1 + ts2 + ts3 + ts4 + ts5) / 5
	return ts_avg

#This function should accept a test score as an
#argument and return a letter grade for the score
def determine_grade(ts_avg):
	if ts_avg <= 100 and ts_avg >= 90:
		grade = "A"
	elif ts_avg <= 89 and ts_avg >= 80:
		grade = "B"
	elif ts_avg <= 79 and ts_avg >= 70:
		grade = "C"
	elif ts_avg <= 69 and ts_avg >= 60:
		grade = "D"
	elif ts_avg < 60:
 		grade = "F"
	return grade

def user_input(num):
	if num == 1:
		num = "first"
	elif num == 2:
		num = "second"
	elif num == 3:
		num = "third"
	elif num == 4:
		num = "fourth"
	elif num == 5:
		num = "fifth"

	input_str = "\nPlease enter the " + num + " test score as a numerical value between 0 and 100.\n"
	try_str = "\nTry again, please.\n"
	script_end_str = "\nScript terminated.\n"
	
	while True:
		try:
			ts = int(input(input_str))
			if ts > 100 or ts < 0:
				print(try_str)
			else:
				break
		except ValueError:
			print(try_str)
		except KeyboardInterrupt:
			print(script_end_str)
			quit()

	return ts

def main():
#call input function to fill variables
##I would rather be able to create a for loop that handles a range
##and creates variables on the fly... Not sure if I can do that or not.
	ts1 = user_input(1)
	ts2 = user_input(2)
	ts3 = user_input(3)
	ts4 = user_input(4)
	ts5 = user_input(5)

#call functions and fill variables
	avg = calc_average(ts1,ts2,ts3,ts4,ts5)
	grade = determine_grade(avg)
#display pleasantly formated output
	header = "\nScore"+"\t"+"Grade"
	print(header)
	print("-"*13 + "\n")
	test_display(ts1)
	test_display(ts2)
	test_display(ts3)
	test_display(ts4)
	test_display(ts5)
	
	print("\nThe average test score is", format(avg,'.1f') + "%", \
		"and the letter grade is", grade + ".\n")

def test_display(var):
	print(str(var) + "\t" + str(determine_grade(var)))

main()
