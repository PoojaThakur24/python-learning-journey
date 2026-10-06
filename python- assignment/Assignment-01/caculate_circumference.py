""" Find the area and circumference of circle. 
Formula: Area of circle: pi * r ** 2
        Circumference of circle: 2 * pi * r

"""

import math

radius = float(input('Enter the radius of the circle: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f'Area of Circle: {area}')
print(f'Circumference of Circle: {circumference}')