numbers = [5, 2, 1, 7, 4, 8, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)