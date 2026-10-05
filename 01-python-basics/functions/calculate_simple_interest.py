""" Calculate Simple Interest
Create a function simple_interest(principal, rate, time) that calculates and returns simple interest."""

def simple_interest(principle,rate,time):
    return principle * rate * time / 100

SI = simple_interest(20000,10,2)

print(f'Simple Interest: {SI}')