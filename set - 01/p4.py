<<<<<<< HEAD
# Write a Python program to find square root of positive number. 

import math
value=int(input("Enter a positve number:"))

if(value>0):
    square= math.sqrt(value)
    print(f"The square root of {value} is {square}.")
else:
    print("Error: Please enter a positive number.")
=======
# Write a Python program to find square root of positive number
import math

num = float(input("Enter a positive number: "))

if num >= 0:
    result = math.sqrt(num)
    print(f"The square root of {num} is: {result}")
else:
    print("Cannot find square root of a negative number.")
>>>>>>> a0dd07bffcf69c77fcf3e744afa67677d405d50f
