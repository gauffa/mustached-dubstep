#Matthew Hall
#ISY 150
#Chapter 5 Exercise 3
#09/30/2013
#Budget Analysis

def main():
#These error statements save a little work in the while-loops
    std_err = "ERROR: Please enter a positive non-zero number."
    exp_err = "ERROR: Please enter a positive number or '0' to end the program."
#The while-loop below allows for input validation before the input is used
    while True:
        try:
            budget = float(input("Please enter your budget for the month.\n"))
            if budget <= 0:
                print(std_err)
            elif budget > 100000:
                print("Seriously, if you have that much money\n" \
                "per month you probably don't need my help with\n" \
                "a budget. As a matter of fact, can we discuss a\n" \
                "long-term loan?\n")
            else:
                break
        except ValueError:
            print(std_err)
#This while-loop also handles input validation
    while True:
        try:
            running_expense = float(input("Please enter your first expense.\n"))
            if running_expense <= 0:
                print(std_err)
            else:
                break
        except ValueError:
            print(std_err)

    okay = running_expense
#This while-loop handles input validation and if the input is acceptable
#maths are performed on the input
    while True:
        try:
            expense = float(input("Please enter your next expense or '0' to end the program.\n"))
            if expense < 0:
                print(exp_err)
            elif expense == 0:
                break
            else:
                running_expense += expense
        except ValueError:
            print(exp_err)
#calculate the difference between the original budget and the sum of expenses is compared and stored
    difference = budget - running_expense
#output is displayed to the user and reminds the user of original inputs
    print("\nYour original budget was","$" + format(budget, '.2f') + ".")
    print("Your total expenses for the month were","$" + format(running_expense, '.2f') + ".")
    if difference > 0:
        print("You have","$" + format(difference,'.2f'), "remaining in your budget.\n")
    elif difference < 0:
#format output to remove negative sign or reword
        print("Your expenses have exceeded your budget by","$" + format(difference * -1,'.2f') + ".\n")
    else:
        print("You have balanced your budget perfectly.\n")

#call main function
main()
