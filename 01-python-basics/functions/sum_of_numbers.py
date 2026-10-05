""" Sum of Natural Numbers
Create a function sum_natural_numbers(n) that returns the sum from 1 to n. """

def sum_natural_numbers(num):

    sum = 0

    for i in range(1,num+1):
        sum = sum + i

    return sum

print(f'Sum of natural numbers is: {sum_natural_numbers(10)}')