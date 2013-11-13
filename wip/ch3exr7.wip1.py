## Matthew Hall
## ISY150
## Chapter 3
## Exercise 7
## Created: 09/08/2013
## Last Modified: 09/18/2013

##A nutritionist who works for a fitness club helps members by evaluating
##diets. As part of her evaluation, she ask members for the number of fat
##and carbohydrate grams they consumed in a day. Then, she calulates the
##number of calories that results from the fat using the following formula:
##calories from fat = fat grams * 9
##next she calculates the number of calories that result from the
##carbohydrates:
##calories from carbs = carb grams * 4
##The nutritionist asked you to write a program that will make these
##calculations.


def main():
#get input from user
    fat_grams = input("How many grams of fat have you consumed today?\n")
    carb_grams = input("How many grams of carbohydrate have you consumed today?\n")
#calculate calories
    fat_cal = (float(fat_grams) * 9)
    carb_cal = (float(carb_grams) * 4)
#display output
    print("The number of fat calories consumed is", format(int(fat_cal)) + ".")
    print("The number of carbohydrate calories consumed is", format(int(carb_cal)) + ".")

    
main()
