""" Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate. """

correct_user_id = '12345'
correct_password = 'thakurpooja24'

for i in range(3):

    user_id = input('Enter User ID: ')
    password = input('Enter Password: ')

    if user_id == correct_user_id and password == correct_password:
        print('Login Successful.')
        break
    else:
        print('Incorrect User ID and Password.')

else:
    print('You have exceeded the maximum number of attempts.')

