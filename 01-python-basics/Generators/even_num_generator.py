""" Even Number Generator
Create a generator function even_numbers(n) that yields all even numbers from 1 to n. """

def even_numbers(n):

    for num in range(1,n+1):

        if num%2==0:
            yield num
    


n = int(input('Enter any number: '))

for num in even_numbers(20):
    print(num) 

