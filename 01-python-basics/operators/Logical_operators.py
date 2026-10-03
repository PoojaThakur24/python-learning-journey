""" Logical operators: and(True if both the conditions true), 
                       or(True if atleast one of the condition is true), 
                       not(Reverse the result.). """

""" 15. Student Result: A student passes if marks are at least 40 in both subjects. 
Check the result using and. """

marks1 = float(input('Enter the marks of the subject 1: '))
marks2 = float(input('Enter the marks of the subject 2: '))

if marks1 >= 40 and marks2 >= 40:
    print('Student Passed.')
else:
    print('Student is Failed.')

