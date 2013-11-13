#Matthew Hall
#ISY 150
#Chapter 6 Exercise 4
#10/07/2013
#Falling Distance

#define formula for distance fallen over time
def falling_distance(time):
	gravity = 9.8
	distance = 0.5 * gravity * time**2
	return distance

def main():
	#print Header
	print("\nTime" + " " * 10 + "Distance")
	print("-" * 28 + "\n")
	#for loop prints output
	for time in range(1,11):
		distance = falling_distance(time)
		#tweaks spacing in output based on number of seconds
		if len(str(time)) == 1:
			spc = 5
		elif len(str(time)) == 2:
			spc = 4
		#makes adjustment for single second output and spacing
		if time == 1:
			time_unit = "second"
			spc = 6
		else:
			time_unit = "seconds"
		#displays output
		print(str(time), time_unit + " " * spc + format(distance,'.2f'),"meters")
	print("\n")
	
main()