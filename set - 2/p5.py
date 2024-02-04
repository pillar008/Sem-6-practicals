#WAP to find maximum of three numbers (nested if-else). 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2:
    if num1 >= num3:
        max_num = num1
    else:
        max_num = num3
else:
    if num2 >= num3:
        max_num = num2
    else:
        max_num = num3

print(f"The maximum of the three numbers is: {max_num}")
