""" Check Element Does Not Exist
Check whether a particular element does not exist using not in. """

numbers = (10,20,30,40,50,60)

element = 80

if element not in numbers:
    print(f'{element} does not exists in the tuple.')
else:
    print(f'{element} exits in the tuple.')