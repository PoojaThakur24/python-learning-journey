""" Write a program to calculate the percentage of student based on marks of any 5
subjects. """

hindi = float(input('Enter the marks scored in Hindi: '))
english = float(input('Enter the marks scored in English: '))
maths = float(input('Enter the marks scored in Maths: '))
science = float(input('Enter the marks scored in Science: '))
marathi = float(input('Enter the marks scored in Marathi: '))

percentage = (hindi + english + maths + science + marathi) / 500 * 100

print(f'Percentage: {percentage}')