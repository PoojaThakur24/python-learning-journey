""" Use copy()
Create a copy of a dictionary and display both dictionaries. """

student = {
    'name' : 'Pooja',
    'age' : 24,
    'marks' : 95,
    'email' : 'thakurpooja60596@gmail.com'
}


student1 = student.copy()

print(student)
print(student1)