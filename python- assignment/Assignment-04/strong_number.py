""" WAP to check if given number Strong Number. """

""" A number is called a Strong Number if the sum of the f
actorials of its digits is equal to the original number. """



num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial = factorial * i

    sum = sum + factorial
    num = num // 10

if sum == original:
    print("It is a Strong Number.")
else:
    print("It is not a Strong Number.")