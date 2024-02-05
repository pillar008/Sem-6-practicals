#WAP to find sum of first N numbers

# for approach
# def sum_n(x):
#     sum=0
#     for i in range(1,x+1,1):
#         sum += i
#     print(f"The sum of first {x} numbers is {sum}")


# formula approach
def sum_n(x):
    sum = (x*(x+1))/2
    print(f"The sum of first {x} numbers is {sum}")

user=int(input("Enter the number:"))
sum_n(user)