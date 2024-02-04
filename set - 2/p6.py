#WAP to calculate the salary of an employee based on following conditions
# (nested if-else):
# 1. if degree = B.E. and experience < 5 years, salary=30000
# 2. if degree = B.E. and experience >= 5 years, salary=40000
# 3. if degree = M.E. and experience < 5 years, salary=50000
# 4. if degree = M.E. and experience >= 5 years, salary= 60000 

degree = input("Enter employee's degree (B.E. or M.E.): ").upper()
experience = int(input("Enter employee's experience in years: "))

if degree == "B.E.":
    if experience < 5:
        salary = 30000
    else:
        salary = 40000
elif degree == "M.E.":
    if experience < 5:
        salary = 50000
    else:
        salary = 60000
else:
    print("Invalid degree entered.")
    exit()

# Print the calculated salary
print(f"The salary of the employee with {degree} degree and {experience} years of experience is: {salary}")
