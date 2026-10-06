""" WAP to calculate area of triangle and rectangle """

length = float(input('Enter the length of the rectangle: '))
breadth = float(input('Enter the breadth of the rectangle: '))

base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

area_of_reactangle = length * breadth
area_of_triangle = (base * height) / 2

print(f'Area of Rectangle: {area_of_reactangle}')
print(f'Area of Triangle: {area_of_triangle}')