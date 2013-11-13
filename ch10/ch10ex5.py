#Matt Hall
#ISY 150
#Chapter 10 Exercise 5
#11/05/2013

#Write a program that reads the contents of a text file. The program should create
#a dictionary in which the keys are the individual words found in the file and
#the values are the number of times each word appears. The program should either
#display the frequency of each word or create a second file containting a list of
#each word and its frequency.

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

def listify(input_str):
	first_list = []
	second_list = []
	#avoid duplicate words based on case-sensitivity
	input_str = input_str.lower()
	#set of characters to remove from list elements
	bad_characters_str = '.,()'
	#split each word into list elements
	first_list = input_str.split()
	#parse first_list for bad characters
	for x in first_list:
		for y in bad_characters_str:
			x = x.strip(y)
		#if element is not all digits append to second_list
		if not x.isdigit():
			second_list.append(x)
	return second_list

def countify(input_list):
	text_count_dict = {}
	for x in input_list:
		y = input_list.count(x)
		text_count_dict[x] = y
	return text_count_dict

def outputify(input_dict):
	print('\n{0:22} {1:14}'.format('Word','Counted'))
	print('-'*30)
	#This lamba stuff is AWESOME! I can make functions on the fly!
	for key, value in sorted(input_dict.items(), key=lambda item : item[1], reverse=True):
		#format output for clarity
		print('{0:20} {1:4}'.format(key,value))

def main():
	text_str = read_file('text.txt')
	text_list = listify(text_str)
	text_dict = countify(text_list)
	outputify(text_dict)


main()
