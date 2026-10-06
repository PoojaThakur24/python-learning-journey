""" Check if Key Exists
Check whether a particular key exists in a dictionary. """

student = {
    'name' : 'Pooja',
    'age' : 24,
    'marks' : 95
}

key = 'name'

if key in student:
    print(f'{key} exits in the dictionary.')
else:
    print(f'{key} does not exits in th dictionary.')