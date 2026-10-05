""" Calculate Factorial
Create a function factorial(number) that returns the factorial of a number. """

def  calculate_factorial(num):
    result = 1

    for i in range(1,num+1):
        result = result * i

    return result

factorial = calculate_factorial(5)

print(f'Factorial of a number is: {factorial}')