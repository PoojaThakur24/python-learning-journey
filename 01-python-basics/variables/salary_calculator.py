""" Salary Calculator

Take basic salary and bonus as input. Calculate total salary. """

basic_salary = float(input('Enter the basic salary: '))
bonus = float(input('Enter the bonus amount: '))

total_salary = basic_salary + bonus

print(f'Basic Salary: {basic_salary}')
print(f'Bonus amount: {bonus}')
print(f'Total Salary: {total_salary}')