#!/usr/bin/python
import base64

'''

This script will allow the user to decode a base64 encoded string multiple times.
    *User inputs a base64 encoded string.
    *The string is decoded by default once, or as many times as entered by the user.
    *The decoded base64 string is output as a result.

Author: Raul Bringas
Date: 4-24-2018

Tested on:
    Python 2.7.14

'''

# Function to decode the user base64 string multiple times
def b64dcode (userString):
    global b64converted
    b64converted = base64.b64decode(userString)

# Store the user input of a base64 encoded string
b64string = raw_input("Enter base 64 encoded string: ")

# Ask the user how many times they want to decode the b64 string
iterations = raw_input("Enter the number of times to decode the b64: ")
# Add if statement to check isnumber otherwise set to 1

print ("\nYou entered the following string: " + b64string)
print ("\nThe string will be decoded " + iterations + " times!\n")

# Print out the result of the decoded base64 string
#print ("Decoded base64 string: " + dCoded)

# Initial function call with user input
b64dcode(b64string)

# Convert user input iterations to int for loop count
count = int(iterations)

# Add a counter to track the amount of attempts to decode
attempts = 0

while (count > 1):
    print ("Next Decoded String:\n " + b64converted)
	attempts += 1
	
	try:
		b64dcode(b64converted)
    
	except:
		print ("\nThe number you entered is too high try using " + str(attempts) + "...")
        break
	
	count -= 1

print ("\nFinal Decoded String: " + b64converted)