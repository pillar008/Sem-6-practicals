#  WAP to check whether entered user ber is prime or not

def prime_check(user):
    if user  == 1:
        print(f"{user} is not a prim number")
    elif user  > 1:
        for i in range(2,user ):
            if (user  % i) == 0:
                print(f"{user} is not a prime number")
                break
        else:
            print(f"{user} is a prime number")
    else:
        print(f"{user} is not a prime number")

user=int(input("Enter the number:"))
prime_check(user)