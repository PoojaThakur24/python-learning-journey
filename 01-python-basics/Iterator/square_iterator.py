""" Square Iterator
Create a custom iterator that generates squares of numbers from 1 to 5. """

class SquareIterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            square = self.num ** 2
            self.num += 1
            return square
        else:
            raise StopIteration

square = SquareIterator()

for i in square:
    print(i)
