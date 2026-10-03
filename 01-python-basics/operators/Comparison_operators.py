""" Comparison operators: ==(Equal to), !=(Not equal to), >(Greater than), <(Less than), 
>=(Greater than and equal to), <=(Less than and equal to). """

""" Greater of Three Numbers: Take two numbers and display which one is greater. """

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if num1 >= num2 and num1 >= num3:
    print(f'{num1} is Greater.')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} is Greater.')
else:
    print(f'{num3} is Greater.')
