# P13-Implement Euclidean Algorithm & Advanced Euclidean Algorithm

def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def advanced_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = advanced_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

# Get input from the user
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Compute the GCD using the Euclidean Algorithm
gcd = euclidean_algorithm(a, b)
print(f"The GCD of {a} and {b} using the Euclidean Algorithm is {gcd}")

# Compute the GCD and Bézout's identity using the Advanced Euclidean Algorithm
gcd, x, y = advanced_euclidean_algorithm(a, b)
print(f"The GCD of {a} and {b} using the Advanced Euclidean Algorithm is {gcd}")
print(f"Bézout's identity: {gcd} = {x} * {a} + {y} * {b}")
