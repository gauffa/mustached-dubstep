########
#Matthew Hall
#Chapter 4
#Exercise 8
#09/22/2013
########

def main():
    #take input from user
    quantity = float(input("Please enter the number of packages to be purchased.\n"))
    #set price
    price = 99
    #set discount_percentage based on input
    if float(quantity) >= 10 and float(quantity) <= 19:
        discount_percentage = 0.8
    elif float(quantity) >= 20 and float(quantity) <= 49:
        discount_percentage_percentage = 0.7
    elif float(quantity) >= 50 and float(quantity) <= 99:
        discount_percentage = 0.6
    elif float(quantity) >= 100:
        discount_percentage = 0.5
    else:
        discount_percentage = 1.0

    #work out some math here
    discount_price = float(price) * float(discount_percentage)
    discount_total = float(discount_price) * float(quantity)
    standard_total = float(quantity) * float(price)
    discount_amount = float(standard_total) - float(discount_total)

    #print output
    print("The amount of the discount is $"\
    	    + format(float(discount_amount),'.2f'))
    print("The cost of the purchase, with the discount, is $"\
    	    + format(float(discount_total),'.2f'))


main()
