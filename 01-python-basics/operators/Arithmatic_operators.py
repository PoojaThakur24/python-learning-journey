"""  Sum of Two Numbers — Take two numbers as input and display their sum. """
# Arithmatic operators - +(Addition), -(subtraction), *(Multiplication), /(Division), //(Floor division), %(Modulus), **(Exponent)(Power)

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponent = num1 ** num2


print(f'Sum of two numbers is: {sum}')
print(f'Difference of two numbers is: {difference}')
print(f'Product of two numbers is: {product}')
print(f'Division of two numbers is: {division}')
print(f'Floor division of two numbers is: {floor_division}')
print(f'Modulus of two numbers is: {modulus}')
print(f'Exponent of two numbers is: {exponent}')
