""" Find Smallest Element
Find the smallest number in a list. """

list = [10,20,30,40,50]

smallest = list[0]

for num in list:

    if num < smallest:
        smallest = num

print(f'Smallest number in the list: {smallest}')