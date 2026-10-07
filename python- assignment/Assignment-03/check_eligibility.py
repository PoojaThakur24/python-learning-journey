""" Write a program to check if person is eligible to marry or not (male age >=21 and
female age>=18) """

age = int(input('Enter your age: '))
gender = input('Enter your gender(male/female): ')

if age >= 21 and gender.lower() == 'male':
    print('You are eligible for marriage.')
elif age >=18 and gender.lower() == 'female':
    print('You are eligible for marriage.')
else:
    print('You are not elligible for marriage.')