class Restaurant:
    """A class modelling a restaurant."""
    def __init__(self, name, cusine_type):
        """Initialize name and type attributes."""
        self.name = name.title()
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        """Display a summary description of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cusine_type}."
        print("\n" + msg) 

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print("\n" + msg)

chiken_town = Restaurant("the chiken town", "seafood")
chiken_town.describe_restaurant()

swiss_hotel = Restaurant("the swiss hotel", "pizza")
swiss_hotel.describe_restaurant()

crown_bakery = Restaurant("the crown bakery", "shawarma")
crown_bakery.describe_restaurant()
