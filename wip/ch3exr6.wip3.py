## Matthew Hall
## ISY150
## Chapter 3
## Exercise 6
## 09/08/2013

##Write a program that calculates and displays a person's BMI. The BMI is
##often used to determine whether a person is overweight or underweight
##for their height.
##A person's BMI is calculated with the following formula:
##BMI = weight * 703 / height^2 (pounds) (inches)

#Identift purpose of script to the user
print("This script will calculate Body Mass Index (BMI) based on user input.")

def user_input:
weight = input("What is your weight in pounds?\n")
height = input("What is your height in inches?\n")

def input_while_validation(weight,height):
    while True: #infinite loop
        try:
            weight = int(weight) or float(weight)
            break #got an integer or float -- break from this infinite loop.
        except ValueError: #uh-oh, didn't get an integer, better try again.
            print("Please use a number. Try again.")

    while True: # infinite loop
        try:
            height = int(height) or float(height)
            break #got an interger or float -- break from this infinite loop.
        except ValueError:
            print("Please use a number. Try again.")

def calc(weight,height):
    #calculate BMI based on user input
    bmi = ((int(weight) * 703) / (int(height)**2))

def scale(weight,height):
    if int(bmi) <= 18:
        bmi_rating = "underwieght"
    elif int(bmi) >= 19 and int(bmi) <= 24:
        bmi_rating = "healthy weight"
    elif int(bmi) >= 25 and int(bmi) <= 29:
        bmi_rating = "overweight"
    elif int(bmi) >= 30:
        bmi_rating = "obese"

def output():
    #print BMI in readable format
    print("\nBased on your weight and height your BMI is", str(int(bmi)) + ".")
    print("Additionaly, based on the BMI scale from 'St. Joseph.org'",\
    "your BMI classifies you as", bmi_rating + ".\n")

input_while_validation(weight,height)
