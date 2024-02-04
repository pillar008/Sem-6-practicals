# Write a Python program to find square root of positive number
import math

num = float(input("Enter a positive number: "))

if num >= 0:
    result = math.sqrt(num)
    print(f"The square root of {num} is: {result}")
else:
    print("Cannot find square root of a negative number.")
