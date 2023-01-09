# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("pigeon", "adra")


# Multiple Function Calls

describe_pet("pigeon", "adra")
describe_pet('camel', 'rizq')


# Order Matters in Positional Arguments

describe_pet('adra', 'pigeon')


# Keyword Arguments

describe_pet(animal_type='camel', pet_name='success')
describe_pet(pet_name='success', animal_type='camel')
