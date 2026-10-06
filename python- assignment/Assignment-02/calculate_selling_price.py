""" WAP to calculate selling price of book based on cost price and discount. """

cost_price = float(input('Enter the cost price of the book: '))
discount = float(input('Enter the discount on book: '))

discount_amount = (cost_price * discount) / 100

selling_price = cost_price - discount_amount

print(f'Selling price: {selling_price}')