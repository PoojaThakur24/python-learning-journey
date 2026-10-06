""" Write a program to swap two numbers using third variable. """

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print(f'Before Swapping: first number: {num1}')
print(f'Before Swapping, Second number: {num2}')

temp = num1
num1 = num2
num2 = temp

print(f'After Swapping: first number: {num1}')
print(f'After Swapping, Second number: {num2}')