# WAP to find sum of N scanned numbers
def main():
    n = int(input("Enter the number of values to sum: "))
    total = sum(float(input(f"Enter number {i+1}: ")) for i in range(n))
    print(f"The sum of the {n} numbers is: {total}")

if __name__ == "__main__":
    main()
# In Python, the if __name__ == "__main__": construct is used to check whether the current script is being run as the main program.