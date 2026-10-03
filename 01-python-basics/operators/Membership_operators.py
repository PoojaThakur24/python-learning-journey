""" Membership Operator: in (Returns true if value is present)
                         not in (Returns true if value is not present) """

student = {
    'name' : 'Pooja',
    'age' : 24,
    'course:' : 'Python'
}

if 'name' in student:
    print(f'name key is present in the dictionary.')
else:
    print(f'name key is not present in the dictionary.')
    