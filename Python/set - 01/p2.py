#Write a Python program to swap two variables using third variable. 

var1 = input("Enter the value of first variable: ")
var2 = input("Enter the value of second variable: ")

print("Before sawpping")
print("First variable =", var1)
print("Second variable =", var2)

temp = var1
var1 = var2
var2 = temp


print("\nAfter swapping:")
print("First variable =", var1)
print("Second variable =", var2)
