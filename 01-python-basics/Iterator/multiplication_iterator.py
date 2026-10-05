""" Multiplication Table Iterator
Create a custom iterator that generates the multiplication table of a given number from 1 to 10 """

class MultiplicationTableIterator:

    def __init__(self, number):
        self.number = number
        self.multiplier = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.multiplier <= 10:
            result = self.number * self.multiplier
            self.multiplier += 1
            return result
        else:
            raise StopIteration


number = int(input("Enter a number: "))

table = MultiplicationTableIterator(number)

for result in table:
    print(result)

