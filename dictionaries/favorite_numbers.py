favorite_numbers = {
    'adra': [27, 32, 100],
    'isata': [23, 40],
    'mlj': [17, 39, 97],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"\t{number}")

# number = favorite_numbers['isata']
# print(f"Isata's favorite number is {number}")
# number = favorite_numbers['binta']
# print(f"Binta's favorite number is {number}")
# number = favorite_numbers['jarai']
# print(f"Jarai's favorite number is {number}.")
