""" Write a program to check if given 3 digit number is a palindrome or not. """

num = int(input('Enter any three digit number: '))

original = num

reverse = 0

while num > 0:

    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(f'{original} is a palindrome number.')
else:
    print(f'{original} is not a palindrome number.')