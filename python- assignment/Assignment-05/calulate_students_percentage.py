""" Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students. """

number_of_student = int(input('Enter number of students: '))

total_percentage = 0

for i in range(1, number_of_student + 1):

    subject1 = int(input('Enter marks for subject1: '))
    subject2 = int(input('Enter marks for subject2: '))
    subject3 = int(input('Enter marks for subject3: '))
    subject4 = int(input('Enter marks for subject4: '))
    subject5 = int(input('Enter marks for subject5: '))

    percentage = (subject1 + subject2 + subject3 + subject4 + subject5) / 500 * 100

    print(f'Percentage: {percentage}')

    total_percentage = total_percentage + percentage

    average_percentage = total_percentage / number_of_student

    print(f'Average Percentage: {average_percentage}')