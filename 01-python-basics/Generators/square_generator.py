""" Square Generator
Create a generator function squares(n) that yields the squares of numbers from 1 to n.

Expected output for n = 5: 1 2 9 16 25 """

def squares(n):

    for num in range(1,n+1):
        yield num ** 2

for num in squares(5):
    print(num)