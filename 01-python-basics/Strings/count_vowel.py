""" Count Vowels
Count the number of vowels in a string. """

str = 'Python Programming'
count = 0

for i in str:

    if i.lower() in 'aeiou':
        count += 1

print(f'Number of vowels in a string is: {count}')
