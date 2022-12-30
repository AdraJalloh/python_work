# A List in a Dictionary
favorite_languages = {
    'haja': ['python', 'swift'],
    'serah': ['dart'],
    'mama': ['dart', 'c++'],
    'rai': ['python', 'javascript'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
