""" 
Student Dictionary

Create a dictionary containing a student's name, age, and marks. Display each key and value. """

student = {
    "name": "Pooja",
    "age": 24,
    "marks": 85
}

# items() is a built-in dictionary method that returns all the key-value pairs in a dictionary.
for key, value in student.items():
    print(f'{key}: {value}')