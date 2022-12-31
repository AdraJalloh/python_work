countries = ["saudi arabia", "qatar", "egypt", "ethiopia", "england", 
"nigeria", "south africa", "united arab emirates", "united states"]

print("The first three countries in the list are:")
for country in countries[:3]:
    print(country.title())

print("\nThe three middle countries in the list are:")
for country in countries[3:6]:
    print(country.title())

print("\nThe last three countries in the list are:")
for country in countries[6:]:
    print(country.title())
