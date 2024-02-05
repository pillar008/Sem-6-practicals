# WAP to find the reverse of given numbers (Example 2564-4652). 

def rev_num(user):
    reversed = 0

    while user != 0:
        digit = user % 10
        reversed = reversed * 10 + digit
        user //= 10

    print(f"Reversed Number: {reversed}")


user=int(input("Enter the number:"))
rev_num(user)