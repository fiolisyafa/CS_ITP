favorite_numbers = {
    "Jordan": [7, 8, 28, 29],
    "Miranda": [13, 18, 3],
    "Catherine": [8, 21, 5],
    "Richard": [11, 12],
    "Tim": [10, 12],
    }

for key, value in favorite_numbers.items():
    print('\n' + key + "'s favorite numbers are:")
    for numbers in value:
        print(numbers)
