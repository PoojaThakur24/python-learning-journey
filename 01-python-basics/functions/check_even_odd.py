""" Check Even or Odd
Create a function check_even_odd(number) that checks whether a number is even or odd. """

def check_even_odd(num):

    if num%2==0:
        print(f'{num} is a even number.')
    else:
        print(f'{num} is a odd number.')

check_even_odd(8)