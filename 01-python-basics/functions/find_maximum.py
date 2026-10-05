""" Find Maximum
Create a function find_max(a, b) that returns the larger of two number """

def find_max(a,b):

    if a > b:
        return a
    else:
        return b
    

maximum = find_max(9,8)

print(f'The larger number is: {maximum}')