# WAP to print the following:
# * * * * *
# * * * *
# * * *
# * *
# * 

rows = int(input("Enter the number of rows: "))
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")