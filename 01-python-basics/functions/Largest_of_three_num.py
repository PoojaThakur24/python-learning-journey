""" Find Largest of Three Numbers
Create a function largest(a, b, c) that returns the largest of three numbers. """

def largest(a,b,c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(f'Largest amoung three number is: {largest(9,7,4)}')