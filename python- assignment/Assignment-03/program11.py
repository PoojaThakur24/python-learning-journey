""" Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full. """


ticket_amount = float(input('Enter ticket amount per person: '))

age1 = int(input('Enter age of person 1: '))
age2 = int(input('Enter age of person 2: '))
age3 = int(input('Enter age of person 3: '))
age4 = int(input('Enter age of person 4: '))
age5 = int(input('Enter age of person 5: '))

total_amount = 0

if age1 < 12:
    total_amount += ticket_amount * 0.70
elif age1 > 59:
    total_amount += ticket_amount * 0.50
else:
    total_amount += ticket_amount

if age2 < 12:
    total_amount += ticket_amount * 0.70
elif age2 > 59:
    total_amount += ticket_amount * 0.50
else:
    total_amount += ticket_amount

if age3 < 12:
    total_amount += ticket_amount * 0.70
elif age3 > 59:
    total_amount += ticket_amount * 0.50
else:
    total_amount += ticket_amount

if age4 < 12:
    total_amount += ticket_amount * 0.70
elif age4 > 59:
    total_amount += ticket_amount * 0.50
else:
    total_amount += ticket_amount

if age5 < 12:
    total_amount += ticket_amount * 0.70
elif age5 > 59:
    total_amount += ticket_amount * 0.50
else:
    total_amount += ticket_amount

print('Total ticket amount:', total_amount)