""" Multiplication Table
Create a function multiplication_table(number) that prints the multiplication table from 1 to 10. """

def multiplication_table(number):

    for i in range(1,11):
        print(f'{number} * {i} = {number*i}')


multiplication_table(9)