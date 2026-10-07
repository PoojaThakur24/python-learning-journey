""" WAP to check if given number is Perfect Number. """

""" Perfect Number: A Perfect Number is a number whose sum of its proper divisors is
equal to the number itself. """

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("It is a Perfect Number.")
else:
    print("It is not a Perfect Number.")