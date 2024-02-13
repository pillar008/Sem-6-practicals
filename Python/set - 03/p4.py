# Write a Python program to print Fibonacci series upto n terms.

def fibonacci(n):

    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        
        if n <= 0:
            print("Please enter a positive integer.")
            return

        fib_series = fibonacci(n)
        print(f"The Fibonacci series up to {n} terms:")
        for term in fib_series:
            print(term, end=" ")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
