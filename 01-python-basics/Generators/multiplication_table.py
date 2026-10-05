""" Multiplication Table Generator
Create a generator function that accepts a number and yields its multiplication table from 1 to 10. """

def multiplication_table(num):

    for i in range(1,11):
        yield num * i

for num in multiplication_table(5):
    print(num)