#!/usr/bin/python
import base64

'''

This script will allow the user to encode a string in base64 format multiple times.
    *User inputs a regular string.
    *The string is encoded by default once, or as many times as entered by the user.
    *The encoded base64 string is output as a result.

Author: Raul Bringas
Date: 4-24-2018

Tested on:
    Python 2.7.14

'''

# Function to decode the user base64 string multiple times
def b64encode (userString):
    global b64converted
    b64converted = base64.b64encode(userString)

# Store the user input of a base64 encoded string
string = raw_input("Enter a string to encode in base64: ")

# Ask the user how many times they want to encode the string
iterations = raw_input("Enter the number of times to encode the string: ")
# Add if statement to check isnumber otherwise set to 1

print ("\nYou entered the following string: " + string)
print ("\nThe string will be encoded " + iterations + " times!\n")


# Initial function call with user input
b64encode(string)

# Convert user input iterations to int for loop count
count = int(iterations)


while (count > 1):
    print ("Next encoded String: " + b64converted)
    b64encode(b64converted)
    count -= 1


print ("\nFinal Encoded String: " + b64converted)