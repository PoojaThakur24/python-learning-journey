""" Write a program to input angles of a triangle and check whether triangle is valid or not. """

angle1 = int(input('Enter the first angle: '))
angle2 = int(input('Enter the second angle: '))
angle3 = int(input('Enter the third angle: '))

angle = angle1 + angle2 + angle3

if angle == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print(f'Triangle is valid.')
else:
    print(f'Triangle is not valid.')