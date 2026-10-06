""" Write a program to convert days into years, weeks and days. """

""" Years = total_days // 365
Remaining days = total_days % 365
Weeks = remaining_days // 7
Days = remaining_days % 7
"""


total_days = int(input("Enter the number of days: "))

years = total_days // 365
remaining_days = total_days % 365

weeks = remaining_days // 7
days = remaining_days % 7

print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {days}")
