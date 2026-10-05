""" Check Prime Number
Create a function is_prime(number) that returns True if the number is prime, otherwise False. """

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2,number):

        if i%2==0:
            return False

    return True

result = is_prime(2)

print("Is the number prime?", result)