###################################################################
#Author:				Matt Hall
#Description:			This script is intended to generate 
#						potential passwords using psuedo-random 
#						numbers
#Date Created:			10/09/2013
#Date Last Modified:	10/09/2013
###################################################################

import random

def random_character(var):
	#attempt to define all characters that can be used for a password
	alpha_lower_chr = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
	alpha_upper_chr = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
	numeric_chr = ('0','1','2','3','4','5','6','7','8','9')
	#some of these special characters may not be appropriate for password use.
	#The " \\ " is of particular concern. ##10/09/2013: This seems to work as intended.
	special_chr = ('!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~')
#consider dual lists for checking repeats, etc.
	almost_all_chr = alpha_lower_chr + alpha_upper_chr + numeric_chr + special_chr

	password = ''

#an issue with this method is duplicate characters can be consecutive
#a check for this needs to be included

	for x in range(var):
		password += random.choice(almost_all_chr)

	return password

def main():
	characters = int(input("Please enter the number of characters you want in your password:\n"))

	password = random_character(characters)

	print("DISCLAIMER: No guarantee of actual security is offered expressly or implicitly.\n"\
		+ "The following is a password generated with a pseudo-random number generator.\n\n" \
		+ password + "\n")

main()