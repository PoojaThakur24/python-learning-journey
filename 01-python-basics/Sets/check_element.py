""" Check Element Exists
Check whether a particular element exists in a set using in. """

set = {10,20,30,40,50}

element = 40

if element in set:
    print(f'{element} exists in a set.')
else:
    print(f'{element} does not exit in the set.')