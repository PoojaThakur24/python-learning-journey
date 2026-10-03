""" Looping: A loop is a control statement that repeatedly executes the code util the condition becomes false. """

""" Multiplication Table: Take a number as input and print its multiplication table from 1 to 10. """

num = int(input('Enter the number you want to print the multiplication table:  '))

for i in range(1,11):
    print(f'{num} * {i} = {num*i}')