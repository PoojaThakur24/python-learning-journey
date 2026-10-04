""" Jump Statements : break, continue, pass.
                    break - Stops the loop completely.
                    continue - Skips the current iteration and moves to the next iteration.
                    pass - Does nothing; it is used as a placeholder for code that you plan to write later.

"""

""" Print numbers from 1 to 10 using a while loop. Stop the loop when the number reaches 5. """


num = 1

while num <= 10:

    print(num)

    if num == 5:
        break

    num += 1