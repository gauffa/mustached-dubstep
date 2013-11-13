## Matthew Hall
## ISY150
## Chapter 3
## Exercise 6
## 09/16/2013

##Write a program that calculates and displays a person's BMI. The BMI is
##often used to determine whether a person is overweight or underweight
##for their height.
##A person's BMI is calculated with the following formula:
##BMI = weight * 703 / height^2 (pounds) (inches)

#Identify purpose of script to the user
print("This script will calculate Body Mass Index (BMI) based on user input.")


def main():
    weight = input("What is your weight in pounds?\n")
    height = input("What is your height in inches?\n")

    bmi = (float(weight) * 703) / (float(height)**2)

    print("With a weight of", str(weight), "pounds and a height of",\
          str(height), "inches you have a BMI of", format(bmi,'0.2f') + ".")

main()
