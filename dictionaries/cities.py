cities = {
    'freetown': {
        'country': 'sierra leone',
        'population': 7092100,
        'fact': 'the transatlantic slave trade.',
        },

    'riyadh': {
        'country': 'saudi arabia',
        'population': 38401000,
        'fact': 'islam origin, oil, the world\s largest desert, etc.',
        },

    'addis ababa': {
        'country': 'ethiopia',
        'population': 113656500,
        'fact': 'the only african country with complete independence.',
        },
    }

for city, info in cities.items():
    print(f'\nCity: {city}')
    country = info['country']
    fact = info['fact']
    population = info['population']

    print(f"\tCountry: {country.title()}")
    print(f"\tFact famous for: {fact.title()}")
    print(f"\tPopulation size: {population}")
