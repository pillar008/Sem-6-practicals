# Write a python program to calculate N!.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        n = int(input("Enter a non-negative integer to calculate its factorial: "))
        
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(n)
            print(f"{n}! = {result}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
