""" Create two variables, `a = 5` and `b = 10`. Swap their values and calculate their sum. """

a = 5
b = 10

print('Before Swapping: ')
print(f'a = {a} b = {b}')

a,b = b,a

print('After Swapping: ')
print(f'a = {a} b = {b}')

sum = a + b

print('Sum of two numbers is: ', sum)