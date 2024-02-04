#WAP to check whether entered number is even or odd.
 
num = input("Enter a number: ")
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
else:
    print("Please enter a valid integer.")
