favorite_languages = {
    'haja': 'python',
    'mama': 'dart',
    'amy': 'swift',
    'rai': 'javascript',
    'serah': 'c++',
    'iye': 'javascript',
    }

friends = ['amy', 'iye', 'dask', 'aisha', 'fortune']
print("List of people taking the poll:")
for name in favorite_languages:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, thank you for responding to the poll.")

if 'dask' not in favorite_languages.keys():
    print("\nDask, please take our poll!")

