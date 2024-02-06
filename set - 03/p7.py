#WAP to print all even numbers between 1 to n except the numbers divisible by 6. 

def func(x):
    for i in range(2,x+1,2):
        if(i%6 != 0):
            print(i)
        else:
            return

user=int(input("Enter a number:"))
func(user)