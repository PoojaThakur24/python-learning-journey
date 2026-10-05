""" Functions: In Python, functions can be classified in a few different ways.
                1. Build-in Functions.
                2. User-Defined Functions.
                3. Functions with Parameters
                4. Functions with Return Value
                5. Anonymous / Lambda Functions
                6. Recursive Functions """

""" 1.Build-in Functions:  1. print(), input()
                           2. type(), id(), isinstance()
                           3. int(), float(), str(), bool()
                           4. len(), sum(), max(), min(), abs(), round()
                           5. range(), sorted(), enumerate(), zip()
                           6. list(), tuple(), set(), dict()
                           7. all(), any()
                           8. map(), filter()
                           9. ord(), chr()
                           10. getattr(), setattr(), hasattr()"""



name = input("Enter your name: ")

# Type conversion functions
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# print() - displays output
print("\nHello,", name)

# type() - returns the data type
print("Type of name:", type(name))
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))

# len() - returns the length
print("Length of name:", len(name))

# Mathematical built-in functions
numbers = [10, 20, 30, 40, 50]

print("\nNumbers:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Absolute value:", abs(-25))
print("Rounded value:", round(12.5678, 2))
print("Power:", pow(2, 3))

# sorted() - sorts the values
print("Sorted numbers:", sorted(numbers, reverse=True))

# range() - generates a sequence of numbers
print("Numbers using range():", list(range(1, 6)))

# bool() - converts a value into Boolean
print("Boolean value of num1:", bool(num1))

# isinstance() - checks the data type
print("Is num1 an integer?", isinstance(num1, int))

values = [True, True, False]

print("Are all values True?", all(values))
print("Is any value True?", any(values))