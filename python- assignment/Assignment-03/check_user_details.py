""" Write a program to check if user has entered correct userid and password. """

correct_userid = '1234'
correct_password = 'thakurpooja24'

userid = input('Enter UserID: ')
password = input('Enter Password: ')

if userid == correct_userid and password == correct_password:
    print('Login Successfull.')
else:
    print('Invalid userid and password.')
