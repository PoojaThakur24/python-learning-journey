""" Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha) """

import random

correct_user_id = '8706'
correct_password = 'pooja123pooja@'

user_id = input('Enter User ID: ')
password = input('Enter Password: ')

if user_id == correct_user_id and password == correct_password:
    print('User ID and Password is correct.')

    ramdom_number = random.randint(1000,9999)

    print('Your Verification number is: ', ramdom_number)

    entered_number = int(input('Enter the above number: '))

    if entered_number == ramdom_number:
        print('Verification Successful. Login Successful.')
    else:
        print('Verification Failed.')

else:
    print('Inavlid username and password.')



