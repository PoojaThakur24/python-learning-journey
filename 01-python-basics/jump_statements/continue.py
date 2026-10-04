""" continue - Skips the current iteration and moves to the next iteration. """

""" Print numbers from 1 to 20, but skip all even numbers using continue. """


for num in range(1,21):

    if num%2==0:
        continue
    else:
        print(num)