# Write a Python program to find sum of n natural numbers without loop.

n = int(input("Enter a positive integer (n): "))

sum = n * (n + 1) // 2

if n > 0:
    print(f"The sum of the first {n} natural numbers is: {sum}")
else:
    print("Please enter a positive integer.")
