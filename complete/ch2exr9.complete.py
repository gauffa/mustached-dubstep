## Matthew Hall
## ISY150
## Chapter 2
## Exercise 9
## 09/05/2013

## Write a program that converts Celsius temperatures to Fahrenheit temperatures.
## The formula is as follows: F = (9/5) * C + 32 ##triple check this formula!
## The program should ask the user to enter a temperature in Celsius, and then
## display the temperateure convereted to Fahrenheit.

#Tell the user what the program/script does
print("\nThis script will convert a temperature from either Fahrenheit or Celsius to the other scale.")

#I decided to define a little subroutine so I could easily call it again if an
#unacceptable input was given.
def scale_conv():
#Ask the user if the temperature being input is Fahrenheit or Celsius
    scale = input("\nWhat scale is your original temperature in [F]ahrenheit or [C]elsius?\n").lower()
#The opscale variable allows for calling a variable instead of using string
#text later in the subroutine
    if scale[0] == "f":
        opscale = "c"
    else:
        opscale = "f"
#calculate a celsius temperature based on the input of the user
#Deduct 32, then multiply by 5, then divide by 9
    if scale == "fahrenheit" or scale == "f":
        print("\nFarenheit it is! Wink-wink!")
        OrgTemp = int(input("So, what is the Farenheit temperature that you would like converted to Celsius?\n"))
        ConvTemp = (OrgTemp - 32) * 5 / 9
        print("\nYour original tempurature of", str(int(OrgTemp)) \
        + chr(176) + str(scale[0].upper()), "converts to", \
        str(int(ConvTemp)) + chr(176) + str(opscale[0].upper()) + ".")
#calculate a fahrenheit temperature based on the input of the user
#Multiply by 9, then divide by 5, then add 32
    elif scale == "celsius" or scale == "c":
        print("\nCelsius it is! Nudge-nudge!")
        OrgTemp = int(input("So, what is the Celsius temperature that you would like converted to Farenheit?\n"))
        ConvTemp = (((OrgTemp * 9) / 5) + 32)
        print("\nYour original tempurature of", str(int(OrgTemp)) \
        + chr(176) + str(scale[0].upper()), "converts to", \
        str(int(ConvTemp)) + chr(176) + str(opscale[0].upper()) + ".")
#tell user they didn't choose an acceptable answer
    else:
        print("Please choose either Farenheit or Celsius. Say no more, eh?")
        scale_conv()
#Run the previously defined subroutine
scale_conv()

##Comments:	
##I could not for the life of me find a way to 'split' input lines the same way
##I can split other lines or print() lines. Any advice on this would be great! Or
##feel free to tell me that spliting lines isn't important... I would like that.
