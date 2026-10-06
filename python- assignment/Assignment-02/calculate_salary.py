""" WAP to calculate total salary of employee based on basic, da=10% of basic,
ta=12% of basic, hra=15% of basic. """

basic = float(input("Enter the basic salary: "))

da = (10 / 100) * basic
ta = (12 / 100) * basic
hra = (15 / 100) * basic

total_salary = basic + da + ta + hra

print(f"DA: {da}")
print(f"TA: {ta}")
print(f"HRA: {hra}")
print(f"Total Salary: {total_salary}")