""" Find Character Frequency
Count how many times each character appears in a string.
"""

text = "python"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)