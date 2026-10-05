""" Cube Generator
Create a generator function cubes(n) that yields the cubes of numbers from 1 to  """

def cube(n):

    for num in range(1,n+1):
        yield num ** 3

for num in cube(10):
    print(num)