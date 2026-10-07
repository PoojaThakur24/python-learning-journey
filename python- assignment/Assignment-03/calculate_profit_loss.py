""" Write a program to calculate profit or loss. """

cost_price = float(input('Enter cost price: '))
selling_price = float(input('Enter selling price: '))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit /cost_price) * 100
    print(f'Profit : {profit}')
    print(f'Profit percentage: {profit_percentage}')
elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print(f'Loss: {loss}')
    print(f'Loss percentage: {loss_percentage}')
else:
    print('No Profit, No Loss.')