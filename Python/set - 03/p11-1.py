# WAP to print the following: 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    num = 1
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
    print()
