# Write a Python program to find area of a rectangle and circle
import math

# Input values for rectangle
rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))

# Calculate and print rectangle area
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area}")

# Input value for circle
circle_radius = float(input("Enter the radius of the circle: "))

# Calculate and print circle area
circle_area = math.pi * circle_radius**2
print(f"The area of the circle is: {circle_area}")
