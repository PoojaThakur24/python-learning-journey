""" Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full. """

no_of_passengers = int(input('Enter number of passangers: '))
ticket_cost = int(input('Enter the ticket cost: '))

total_amount = 0

for i in range(1, no_of_passengers + 1):

    age = int(input('Enter age of passengers: '))

    if age <= 12:
        amount = ticket_cost - (ticket_cost * 30) /100
    elif age > 59:
        amount = ticket_cost - ( ticket_cost * 50) /100
    else:
        amount = ticket_cost

    total_amount = total_amount + amount

print(f'Total ticket amount: {total_amount}')
