# Write a Python program to find N!. 


# rescursive approach
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# if-else and loop approach
def factorial(x):
    fact=1
    if x < 0:
        print("Factorial does not exist for negative numbers")
    elif x == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,x+1,1):
            fact *= i
        print(f"The factorial of {x} is {fact}")



user=int(input("Enter the number:"))
factorial(user)