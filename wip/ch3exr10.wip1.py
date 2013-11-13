## Matthew Hall
## ISY150
## Chapter 3
## Exercise 10
## 09/08/2013
## Last modified: 09/18/2013

## A retail company must file a monthly sales tax report listing the total
## sales for the month, and the amount of state and county sales tax collected.
## The state sales tax rate is 4 percent and the county sales tax rate is
## 2 percent. Write a program that asks the user to enter the total sales
## for the month. From this figure, the application should calculate and
## dispaly the following: amount of county sales tax, smount of state sales
## tax, total sales tax(county plus state).

def main():
#get input from user
    sales = float(input("What is the amount of sales for the month?\n"))
#calculate sales tax
    county_sales_tax = float(sales) * 0.02
    state_sales_tax = float(sales) * 0.04
    total_sales_tax = float(state_sales_tax) + float(county_sales_tax)
#display totals
    print("The total amount of sales is $" + format(float(sales),'.2f') + ".")
    print("The county sales tax for the sales amount is $" + format(float(county_sales_tax),'.2f') + ".")
    print("The state sales tax for the sales amount is $" + format(float(state_sales_tax),'.2f') + ".")
    print("The total sales tax for the sales amount is $" + format(float(total_sales_tax),'.2f') + ".")


main()
