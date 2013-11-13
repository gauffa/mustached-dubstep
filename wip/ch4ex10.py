## Matthew Hall
## ISY150
## Chapter 4
## Exercise 10
## 09/23/2013

##Write a program that calculates and displays a person's BMI. The BMI is
##often used to determine whether a person is overweight or underweight
##for their height.
##A person's BMI is calculated with the following formula:
##BMI = weight * 703 / height^2 (pounds) (inches)

#Identify purpose of script to the user
print("This script will calculate Body Mass Index", \
"(BMI) based on user input.")

def main():
	#get input from user
	weight = input("What is your weight in pounds?\n")
	height = input("What is your height in inches?\n")
	#math the input
	bmi = (float(weight) * 703) / (float(height)**2)
	#determine health level based on bmi
	if float(bmi) > 18.5 and float(bmi) < 25:
		health = "optimal weight"
	elif float(bmi) < 18.5:
		health = "underweight"
	elif float(bmi) > 25:
		health = "overweight"
	#provide output of math in readable format
	print("With a weight of", str(weight), "pounds and a height of",\
		str(height), "inches you have a BMI of", \
		format(bmi,'0.2f') + ".\nYou are", health + ".")

main()
