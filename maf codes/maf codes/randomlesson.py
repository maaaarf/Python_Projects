numbers = [12, 45, 78, 23, 56, 89, 91, 34]

largest = numbers[0]

for big in numbers:
    if big > largest:
        largest = big

print(f"The largest number is {largest}")