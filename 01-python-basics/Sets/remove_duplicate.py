""" Remove Duplicates from a List
Given a list with duplicate elements, use a set to create a list containing only unique elements. """

numbers = [10,20,30,40,50,60,60,50,40,30,20,10]

set = set(numbers)

new_list = list(set)
print(new_list)