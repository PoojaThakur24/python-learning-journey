""" WAP to print Armstrong number within a given range """

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    original = num
    total = 0
    digits = len(str(num))

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        print(original)