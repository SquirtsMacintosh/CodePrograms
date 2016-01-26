#Find Pi to any specific digit that the user specifies
#Created by Zach Martin

import math

#asks the user how many digits of pie they would like to see
digits = int(raw_input("Number of iterations to generate pi?: "))

#creates the number pi if given a large number of iterations
def Pi(double): 
	pi = 0.0
	for i in range(0,double):
		pi += (math.pow(-1,i))/(2*i+1) 
	return 4*pi
	
print Pi(digits)

#add code to give amounts of precision

