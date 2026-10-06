""" Write a program to swap two numbers without using third variable. """

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

num1,num2 = num2,num1

print(f'After Swapping, first number: {num1}')
print(f'After Swapping, second number: {num2}')