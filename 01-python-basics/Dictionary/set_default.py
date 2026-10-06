""" Use setdefault()
Add a key only if it does not already exist. """

student = {
    'name': 'Pooja',
    'age': 24
}

student.setdefault('marks', 95)

print(student)
