""" Even Number Iterator
Create a custom iterator that generates even numbers from 2 to 20. """

class EvenNumberIterator:

    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 20:
            even = self.num
            self.num += 2
            return even
        else:
            raise StopIteration

even = EvenNumberIterator()

for i in even:
    print(i)


