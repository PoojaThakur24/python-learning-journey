""" Write a program to input any alphabet and check whether it is vowel or consonant. """

alphabet = input('Enter any alphabet: ')

if alphabet in 'aeiou':
    print(f'{alphabet} is a vowel.')
else:
    print(f'{alphabet} is a consonant.')