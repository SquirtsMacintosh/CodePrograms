# Word Counter that imports a file and counts the number of words
# Created by Zach Martin

from TKinter import *

# explicitly opens a file to count it's words
fileExample = open('example.txt','r')

#starts with previous character being space set to true 
isSpace = True
wordCount = 0

# iterates through each line within the given files and counts each word ignoring spaces
for line in fileExample:
	for i, x in enumerate(line): 
		if line[i] is ' ':	
			isSpace = True
		else:
			if isSpace:
				wordCount = wordCount + 1
				isSpace = False

print wordCount	

# closes previously opened file
fileExample.close()
