""" Write a program to enter P, T, R and calculate Compound Interest. 
Formula : The standard compound interest formula is:

A = priciple * (1 + rate /100) ** time
 

Where:

P = Principal amount

R = Rate of interest per year (%)

T = Time in years

A = Final amount

Compound Interest
Once you calculate the final amount:

CI=A - P

 """

principal = 10000
rate = 5
time = 2

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print(f"Compound Interest: ₹{compound_interest}")
print(f"Total Amount: ₹{amount}")