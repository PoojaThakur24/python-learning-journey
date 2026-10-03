""" if..elif..else: This statement is used to check multiple condition. """

""" Grade Calculator: Take marks and display a grade: 90 - 100: A
                                                       80 - 89: B
                                                       70 - 79: C
                                                       60 - 69: D
                                                       Below 60: F """

marks = float(input('Enter the marks of the student: '))

if marks >= 90 and marks <= 100:
    print('Grade A')
elif marks >= 80 and marks <= 90:
    print('Grade B')
elif marks >= 70 and marks <= 79:
    print('Grade C')
elif marks >= 60 and marks <=69:
    print('Grade D')
else:
    print('Failed.')