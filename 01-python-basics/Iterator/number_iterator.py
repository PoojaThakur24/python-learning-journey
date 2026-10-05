""" Number Iterator
Create a custom iterator that generates numbers from 1 to 10. """

class NumberIterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

number = NumberIterator()

for i in number:
    print(i)