""" Simple Interest

Store principal, rate, and time in variables. 
Calculate simple interest using `(principal * rate * time) / 100`. """

principal = int(input('Enter the principle amount: '))
rate_of_interest = float(input('Enter rate of interest: '))
no_of_years = int(input('Enter the number of years: '))

simple_interest = (principal * rate_of_interest * no_of_years) / 100

print('Simple Interest: ', simple_interest)