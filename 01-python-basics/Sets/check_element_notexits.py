""" Check Element Does Not Exist
Check whether an element does not exist using not in. """

set = {10,20,30,40,50,60,70,80,90,100}

element = 110

if element not in set:
    print(f'{element} does not exits in the set.')
else:
    print(f'{element} exits in the set.')