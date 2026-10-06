""" Check Element Exists
Check whether a particular element exists in a tuple using the in operator. """

numbers = (10,20,30,40,50,60,70,80,90,100)

element = 30

if element in numbers:
    print(f'{element} exits in the tuple.')
else:
    print(f'{element} does not exits in the tuple.')