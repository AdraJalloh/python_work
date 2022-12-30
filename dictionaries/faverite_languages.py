# A Dictionary of Similar Objects
favorite_languages = {
    'rai': 'javascript',
    'serah': 'dart',
    'mama': 'swift',
    'haja': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())


friends = ["haja", "serah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


if 'Amy' not in favorite_languages.keys():
    print("\nAmy, please take our poll!")


# Looping Through a Dictionary's Keys in a Particular Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# To not repeat a language, we use a set.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
