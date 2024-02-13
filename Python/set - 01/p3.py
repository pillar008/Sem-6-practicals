# Write a Python program to swap two variables without third variable

var1 = float(input("Enter the value for 'Variable 1': "))
var2 = float(input("\nEnter the value for 'Variable 2': "))

print("\nBefore swapping:")
print("\nVariable 1:", var1)
print("\nVariable 2:", var2)

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print("\nAfter swapping:")
print("\nVariable 1:", var1)
print("\nVariable 2:", var2)
