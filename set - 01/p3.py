# Write a Python program to swap two variables without third variable

var1 = 10
var2 = 20

print("Before swapping:")
print("Variable 1:", var1)
print("Variable 2:", var2)

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print("After swapping:")
print("Variable 1:", var1)
print("Variable 2:", var2)
