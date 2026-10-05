""" Dictionary Iterator
Create a dictionary containing three student details. 
Create an iterator for the dictionary and print each key using next(). """

student = {
    'name' : 'Pooja',
    'age' : 24,
    'marks' : 100
}

iterator = iter(student)

print(next(iterator))
print(next(iterator))
print(next(iterator))




