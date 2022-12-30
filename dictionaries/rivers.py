rivers = {
    'amazon': 'brazil, peru',
    'mississippi': 'united states',
    'nile': 'egypt', 
    'yangtze': 'china',
    'zambezi': 'zambia, zimbabwe',
    }

for river, country in rivers.items(): 
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe three famous rivers in the world are as follows:")
for river in rivers:
    print('- ' + river.title())

print("\nAnd the countries where you can find them laying:")
for country in rivers.values():
    print('- ' + country.title())
