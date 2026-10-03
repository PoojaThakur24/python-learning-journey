""" Set Operations

Create two sets and display their union, intersection, and difference. """

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

print(f'First Set: {set1}')
print(f'Second Set: {set2}')

print(f'Union: {set1.union(set2)}')
print(f'Intersection: {set1.intersection(set2)}')
print(f'Difference: {set1.difference(set2)}')

