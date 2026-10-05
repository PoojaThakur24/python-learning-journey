""" Simple Generator
Create a generator function numbers() that yields numbers from 1 to 5. """

def numbers():
    for i in range(1, 6):
        yield i


obj = numbers()

for num in obj:
    print(num)