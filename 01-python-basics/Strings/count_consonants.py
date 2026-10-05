""" Count Consonants
Count the number of consonants in a string. """

str = 'Python Programming'
count = 0

for i in str:

    if i.isalpha() and  i.lower() not in 'aeiou':
        count += 1

print(f'Number of consonants in the string: {count}')
