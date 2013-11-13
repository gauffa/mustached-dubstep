#Matthew Hall
#ISY150
#Chapter 5 Exercise 6
#10/02/2013
#Celsius to Farenheit Table

def main():
#define constants
    temp_range = 20

#print 'header' for table
    print("\nFahrenheit\tCelsius")
    print("----------------------")

#maths to determine a range of temps
    for celsius in range (0, temp_range + 1, 1):#'c_temp + 1' ensure implied range
        farenheit = (((9/5) * celsius) + 32)
        print(format(farenheit,'.1f'),'\t\t',celsius)
    print("")#blank line at end of table


#call main function
main()
