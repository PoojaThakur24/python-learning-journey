""" Program to Find the Roots of a Quadratic Equation """


import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = b ** 2 - 4 * a * c

root1 = (-b + math.sqrt(discriminant)) / (2 * a)
root2 = (-b - math.sqrt(discriminant)) / (2 * a)

print(f"First root: {root1}")
print(f"Second root: {root2}")