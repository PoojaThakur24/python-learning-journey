""" Input 5 subject marks from user and display grade(eg.First class,Second class ..) """

subject1= int(input('Enter marks for subject1: '))
subject2= int(input('Enter marks for subject1: '))
subject3= int(input('Enter marks for subject1: '))
subject4= int(input('Enter marks for subject1: '))
subject5= int(input('Enter marks for subject1: '))

percentage = (subject1 + subject2 + subject3 + subject4 + subject5) / 500 * 100

print('Percentage:', percentage)

if percentage >= 75:
    print('Grade: Distinction.')

elif percentage >= 60:
    print('Grade: First Class.')

elif percentage >= 50:
    print('Grade: Second Class.')

elif percentage >= 35:
    print('Grade: Pass Class.')

else:
    print('Failed.')