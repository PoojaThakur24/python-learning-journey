""" Product Price Calculator

Store an item's price and discount percentage. Calculate the discount amount and final price. """

item_price = float(input('Enter the items price: ' ))
discount_percentage = float(input('Enter the discount price: '))

discount_amount = item_price * discount_percentage / 100

final_price = item_price - discount_amount

print(f'Discount amount: {discount_amount}')
print(f'Final price: {final_price}')

