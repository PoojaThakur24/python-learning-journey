""" Check Palindrome
Create a function is_palindrome(text) that checks whether a string is a palindrome. """

def is_palindrome(text):

    original = text

    if original == text[::-1]:
        print('String is a Palindrome.')
    else:
        print('String is not a palindrome.')

is_palindrome('madam')