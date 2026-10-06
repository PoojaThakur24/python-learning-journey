"""WAP to find minimum number of notes needed for an amount."""

amount = int(input("Enter the amount: "))

notes_500 = amount // 500
amount = amount % 500

notes_200 = amount // 200
amount = amount % 200

notes_100 = amount // 100
amount = amount % 100

notes_50 = amount // 50
amount = amount % 50

notes_20 = amount // 20
amount = amount % 20

notes_10 = amount // 10
amount = amount % 10

total_notes = notes_500 + notes_200 + notes_100 + notes_50 + notes_20 + notes_10

print(f"₹500 notes: {notes_500}")
print(f"₹200 notes: {notes_200}")
print(f"₹100 notes: {notes_100}")
print(f"₹50 notes: {notes_50}")
print(f"₹20 notes: {notes_20}")
print(f"₹10 notes: {notes_10}")
print(f"Minimum number of notes: {total_notes}")