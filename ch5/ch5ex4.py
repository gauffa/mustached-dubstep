#Matthew Hall
#ISY150
#Chapter 5 Exercise 4
#10/02/2013
#Distance Traveled

def main():
#Error statements
    std_err = "Please enter a non-zero, positive, whole number."
#input validation loop no negative numbers, no zero numbers
    while True:
        try:
            speed = int(input("What is the speed of the vehicle?\n"))
            if speed <= 0:
                print(std_err)
            else:
                break
        except ValueError:
            print(std_err)
#input validation loop no negative numbers, no zero numbers
    while True:
        try:
            time = int(input("How many hours has the vehicle traveled?\n"))
            if time <= 0:
                print(std_err)
            else:
                break
        except ValueError:
            print(std_err)



#print 'header' for table
    print("\nHour\tMiles")
    print("-------------")

#maths to determine distance over time
    for hour in range(1, time + 1, 1): #'time + 1' ensures we output implied hours
        distance = speed * hour
        print (hour, '\t', distance)
    print("") #blank line at end of table

main()
