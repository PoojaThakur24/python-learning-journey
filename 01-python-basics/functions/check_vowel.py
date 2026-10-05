""" Count Vowels
Create a function count_vowels(text) that counts and returns the number of vowels. """

def count_vowels(text):

    count = 0

    for i in text:

        if i in 'aeiou':
            count += 1

    return count

print(f'Number of Vowels in a string: {count_vowels('Pooja')}')