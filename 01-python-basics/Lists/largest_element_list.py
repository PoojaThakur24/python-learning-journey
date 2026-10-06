""" Find Largest Element
Find the largest number in a list. """

list = [100,120,90,45,27]

largest = list[0]

for num in list:

    if num > largest:
        largest = num

print(f'The larger number in the list is: {largest}')
        