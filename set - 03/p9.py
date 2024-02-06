#Write a python program to check whether given number is Armstrong or not. 

def Armstrong(x):
    sum = 0
    temp = x
    while temp > 0:
        value = temp % 10
        sum += value ** 3
        temp //= 10

    if x == sum:
        print(x,"is an Armstrong number")
    else:
        print(x,"is not an Armstrong number")


user = int(input("Enter a number: "))
Armstrong(user)