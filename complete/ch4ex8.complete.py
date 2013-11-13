########
#Matthew Hall
#Chapter 4
#Exercise 8
#Created: 09/22/2013
#Last Mod: 09/25/2013
########

def main():
    #take input from user
    quantity = float(input("Please enter the number of packages to be purchased.\n"))
    #set price
    price = 99
    #set discount_percentage based on input
    if quantity >= 10 and quantity <= 19:
        discount_percentage = 0.8
    elif quantity >= 20 and quantity <= 49:
        discount_percentage = 0.7
    elif quantity >= 50 and quantity <= 99:
        discount_percentage = 0.6
    elif quantity >= 100:
        discount_percentage = 0.5
    else:
        discount_percentage = 1.0

    #work out some math here
    discount_price = float(price * discount_percentage)
    discount_total = float(discount_price * quantity)
    standard_total = float(quantity * price)
    discount_amount = float(standard_total - discount_total)

    #print output
    print("The amount of the discount is $" + format(discount_amount,',.2f'))
    print("The cost of the discounted purchase is $" + format(discount_total,',.2f'))


main()
