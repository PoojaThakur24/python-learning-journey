""" Countdown Iterator
Create a custom iterator that starts from 5 and returns: 5 4 3 2 1 """

class CountdownIterator:

    def __init__(self):
        self.num = 5

    def __iter__(self):
        return self

    def __next__(self):

        if self.num >= 1:
            value = self.num
            self.num -= 1
            return value
        else:
            raise StopIteration

countdown = CountdownIterator()

for i in countdown:
    print(i)