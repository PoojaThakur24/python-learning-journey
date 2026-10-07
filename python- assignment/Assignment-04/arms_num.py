# WAP to check if given number is Armstrong number or not

num = int(input("Enter a number: "))

original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("It is an Armstrong Number.")
else:
    print("It is not an Armstrong Number.")