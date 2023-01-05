def city_country(city, country):
    """Return a string like 👉 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country("santiago", "chile")
print(city)
city = city_country("freetown", "salone")
print(city)
city = city_country("conakry", "guinea")
print(city)
