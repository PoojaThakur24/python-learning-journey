""" 
Use get() with Default Value
Try to access a key that does not exist and display "Key not found" instead of getting an error. """

student = {
    'name': 'Pooja',
    'age': 24,
    'marks': 95
}

result = student.get('city', 'Key not found')

print(result) 