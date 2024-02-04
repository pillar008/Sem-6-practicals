#WAP to find roots of quadratic equations if roots are real. 

import math

a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if roots are real
if discriminant >= 0:
    # Calculate the roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
else:
    print("The roots are complex (non-real).")
