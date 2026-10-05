""" Odd Number Iterator
Create a custom iterator that generates odd numbers from 1 to 19. """

class OddNumberIterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 20:
            odd = self.num
            self.num += 2
            return odd
        else:
            raise StopIteration

odd = OddNumberIterator()

for i in odd:
    print(i)