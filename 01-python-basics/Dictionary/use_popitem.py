""" Use popitem()
Remove the last inserted key-value pair using popitem(). """

student = {
    'name' : 'Pooja',
    'age' : 24,
    'marks' : 95,
    'city' : 'Nagpur'
}

student.popitem() # popitem() removes the last inserted key-value pair

print(student)