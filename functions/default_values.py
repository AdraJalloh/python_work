# Default Values

def describe_pet(pet_name, animal_type='camel'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="success")


# Equivalent Function Calls
# A camel named Success
describe_pet("Success")
describe_pet(pet_name='success')

# A rabbit named Adra
describe_pet("adra", "rabbit")
describe_pet(pet_name="adra", animal_type="rabbit")
describe_pet(animal_type="rabbit", pet_name="adra")
