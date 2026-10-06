""" Write a program to enter P, T, R and calculate simple Interest. """

principle = float(input('Enter the principle amount: '))
rate = float(input('Enter the rate of interest: '))
time = float(input('Enter the time: '))

simple_interest = (principle * rate * time) /100

print(f'Simple Interest: {simple_interest}')