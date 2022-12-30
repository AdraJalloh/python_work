favorite_places = {
    'adra': ['addis ababa', 'paris', 'riyadh'],
    'haja': ['cairo', 'doha', 'london'],
    'rai': ['cape town', 'mecca', 'madrid'],
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are as follows:")
    for place in places:
        print(f'\t{place.title()}')
