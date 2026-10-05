""" Odd Number Generator
Create a generator function odd_numbers(n) that yields all odd numbers from 1 to n. """

def odd_numbers(n):

    for num in range(1,n+1):

        if num%2!=0:
            yield num

for num in odd_numbers(20):
    print(num)