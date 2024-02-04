# Write a Python program to find square root of positive number. 

import math
value=int(input("Enter a positve number:"))

if(value>0):
    square= math.sqrt(value)
    print("\nThe square root of {value} is {square}.")
else:
    print("\nError: Please enter a positive number.")
