# Write a python program to check whether given number is Palindrome or not

def palindrome(x):
    temp=x
    rev=0
    while(x>0):
        dig=x%10
        rev=rev*10+dig
        x=x//10
    if(temp==rev):
        print(f"{temp} is a palindrome!")
    else:
        print(f"{temp} isn't a palindrome!")


user=int(input("Enter number:"))
palindrome(user)