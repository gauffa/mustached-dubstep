## Matthew Hall
## ISY150
## Chapter 2
## Exercise 7
## 09/05/2013

## A car's miles-per-gallon (MPG) can be calculated with the following formula:
## MPG = Miles driven/Gallons of gas used
## Write a program that asks the user for the number of miles driven
## and the gallons of gas used. It should calculatre the car's MPG
## and display the result.

#Tell user what the program/script does
print("\nThis script calculates an average 'Miles-Per-Gallon' for a vehicle based on user input.")

#Assign variables and take input from the user
MilesDriven = float(input("\nHow many miles were driven?\n"))
GasUsed = float(input("\nHow many gallons of gasoline were used?\n"))

#Calculate the miles per gallon
MPG = MilesDriven / GasUsed

#Make fun of user for having low miles-per-gallon
if MPG <= 10:
	Comment = "What are you driving?! An M1A1 Abrahms Main Battle Tank!\n"
elif MPG >= 10 and MPG <= 40:
	Comment = "I suppose that's reasonable mileage. You might want to adjust your driving habits a little to improve your effeciency.\n"
#Boggle at users exceptionally efficient vehicle--or lies!
else:
	Comment = "That's pretty decent milelage, actually. You must own a Prius. That or you lied...!\n"

#Display miles per gallon based on user input
print("\nYour vehicle gets about " + str(MPG) + " miles per gallon of gasoline.", Comment)


