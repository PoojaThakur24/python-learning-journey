""" Shopping Bill

Ask for the price and quantity of an item. Calculate the total bill. """

quantity_of_item = int(input('Enter the quantity of an item: '))
price_of_item = float(input('Enter the price of item: '))

total_bill = price_of_item * quantity_of_item

print('Total Bill: ', total_bill)