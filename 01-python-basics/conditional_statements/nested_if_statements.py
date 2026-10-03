""" Nested..if..statement: Nested if means placing one if statement inside another if statement. """

""" ATM Withdrawal: Ask for the account balance and withdrawal amount. 
Allow the withdrawal only if the amount is positive and the balance is sufficient. """

balance = float(input('Enter the account balance: '))
withdrawal_amount = float(input('Enter the amount you want to withdraw: '))

if withdrawal_amount > 0:
    if balance > withdrawal_amount:
        balance -= withdrawal_amount
        print('Amount is withdrawn successfully.')
        print(f'Remaining balance: {balance}')
    else:
        print('Insufficient account balance.')
else:
    print('Inavlid withdrawal amount.')