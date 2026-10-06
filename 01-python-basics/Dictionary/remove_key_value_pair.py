""" Remove a Key-Value Pair
Remove a particular key from a dictionary. """

''' We can remove elements from the dictionary using del and pop() method. '''

student = {
    'name' : 'Pooja',
    'age' : 24,
    'marks' : 95,
    'email' : 'thakurpooja60596@gmail.com'
}

""" del student['age']

print(student) """

student.pop('age')

print(student)