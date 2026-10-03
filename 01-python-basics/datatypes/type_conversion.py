""" Type Conversion

Take a number as a string, convert it into an integer and a float, and display 
both results with their types. """

num = input('Enter any number: ')

int_num = int(num)
float_num = float(num)

print(f'Integer number: {int_num}')
print(f'Type: {type(int_num)}')

print(f'Float number: {float_num}')
print(f'Type: {type(float_num)}')