def describe_city(city, country='Salone'):
    """Discribing a city."""
    # message = city.title() + " is in " + country.title() + "."
    message = f"{city.title()} is in {country.title()}."
    print(message)

describe_city('makeni')
describe_city('freetown', 'salone')
describe_city('bounce island')
