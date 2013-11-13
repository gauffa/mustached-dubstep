## Matthew Hall
## ISY150
## Chapter 2
## Exercise 6
## 09/05/2013

##Write a program that will ask the user to enter the amount of a purchase. The program should
##then compute the state and county sales tax. Assume the state sales tax is 4 percent and the
##county sales tax is 2 percent. The program should displa the amount of the purchase, the state
##sales tax, the county sales tax, the total sales tax and the total of the sale (which is the
##sum of the amount of purchase plus the total sales tax.
##Hint: use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.

#Tell user what the program/script does
print("\nThis script will calculate sales tax of a purchase based on predefined tax values.")

#'Declare' and input values for sales tax variables
StateSalesTaxRate = float(0.04)
CountySalesTaxRate = float(0.02)

#Request purchase amount from user
##some input validation should be present here to make certain text or other invalid data hasn't been used
PurchaseAmt = float(input("\nWhat is the amount of your purchase? \n"))

#calculate sales tax amounts, totals, etc.
StateSalesTaxAmt = StateSalesTaxRate * PurchaseAmt
CountySalesTaxAmt = CountySalesTaxRate * PurchaseAmt
TotalSalesTaxAmt = StateSalesTaxAmt + CountySalesTaxAmt
TotalPurchaseAmt = PurchaseAmt + TotalSalesTaxAmt

#display totals to user
##the '\n' end line statements allow for a single print function call and help to 'format' the apperance of
##the output
print("\nThe state sales tax, currently", format(StateSalesTaxRate, '.0%') + ", is $" + format(StateSalesTaxAmt, ',.2f')+ \
"\nThe county sales tax, currently", format(CountySalesTaxRate, '.0%') + ", is $" + format(CountySalesTaxAmt, ',.2f') + \
"\nThe total sales tax is $" + format(TotalSalesTaxAmt, ',.2f') + \
"\n\nThe total cost of the purchase including all sales tax is $" + format(TotalPurchaseAmt, ',.2f') + "\n")

##Is one print statement considered more efficient or does this just make a mess?
