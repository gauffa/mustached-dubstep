#Matt Hall
#ISY 150
#Chapter 9 Exercise 7
#10/27/2013

#Write a program that reads the file's contents and determines the following:

#The number of uppercase letters in the file
#The number of lowercase letters in the file
#The number of digits in the file
#The number of whitespace characters in the file

def read_file(txt_file):
	ok = False
	while ok == False:
		try:
			#include checks for file not existing, etc
			txt_file_obj = open(txt_file,'r')
			txt_file_str = txt_file_obj.read()
			txt_file_obj.close()
			#return string of file
			return txt_file_str
			ok = True
		#include appropriate exceptions
		except ValueError:
			print('stuff is broken?')

def convert_count_string(txt_str):
	uppercase_count = 0
	lowercase_count = 0
	digits_count = 0
	whitespace_count = 0

	for x in txt_str:
		if x.isupper():
			uppercase_count += 1
		elif x.islower():
			lowercase_count += 1
		elif x.isdigit():
			digits_count += 1
		elif x.isspace():
			whitespace_count += 1
		else:
			pass

	return uppercase_count,lowercase_count,digits_count,whitespace_count

def main():
	txt_file_str = read_file('text.txt')
	up_count,low_count,digi_count,spc_count = convert_count_string(txt_file_str)
	print('The following statistics were ascertained about the text file:\n'+'Uppercase: '\
		+str(up_count)+'\n'+'Lowercase: '+str(low_count)+'\n'+'Numbers: '+str(digi_count)+\
		'\n'+'Whitespace: '+str(spc_count)+'\n')

main()
