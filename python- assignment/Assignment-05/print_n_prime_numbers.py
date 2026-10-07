""" Write a program to print first n prime numbers. """

n = int(input('Enter any number: '))

for i in range(2, n+1):

    for num in range(2, i):

        if i%num==0:
            print(num)
        
            