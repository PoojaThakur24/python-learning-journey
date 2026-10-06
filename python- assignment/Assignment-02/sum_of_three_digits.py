""" Find the sum of three-digit number. """

num = int(input('Enter any three digit number: '))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

sum = hundreds + tens +ones

print(f'Sum of three digit number: {sum}')


