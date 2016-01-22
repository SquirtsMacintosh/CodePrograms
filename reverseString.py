# Takes an input for a string and reverses it
# Created by Zach Martin

#asks for string to be reversed
originalString = raw_input("Please enter a string you want reversed: ")
stringSize = len(originalString) #counts the size of the string

#loops through string and reverses it
reversedString = ''
for i, x in enumerate(originalString):
	reversedString = reversedString + originalString[(stringSize - 1) - i]
	
#prints the reversed string	
print "Your string reversed is: " + reversedString
