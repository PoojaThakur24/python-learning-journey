""" Create an Iterator from a List
Create a list of five numbers. Convert the list into an iterator using iter() and print each element using next(). """

list1 = [10,20,30,40,50]

iterator = iter(list1)

print(next(iterator))

for i in iterator:
    print(i)