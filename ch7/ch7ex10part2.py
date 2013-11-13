#Matt Hall
#ISY 150
#Chapter 7 Exercise 10
#10/14/2013

#Program that reads the records from the 'golf.txt' file and displays them.

def main():
	scorecard_file = open('golf.txt','r')
	#print heading for scorecard_file
	header1 = "Player Name"+"\t"+"Score"
	header2 = (len(header1)+4)*"-"
	print(header1+'\n'+header2)
	for x in scorecard_file:
		line = str(x)
		line = line.rstrip('\n')
		print(line)
	scorecard_file.close()

main()
