class Restaurant:
    """A class modelling a restaurant."""
    def __init__(self, name, cusine_type):
        """Initialize name and type attributes."""
        self.name = name.title()
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary description of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cusine_type}."
        print("\n" + msg) 

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. We welcome y'all!"
        print("\n" + msg)

    def restaurant(self):
        """Print the number of customers served by the restaurant."""
        print(f"The restaurant has served {self.number_served} customers.")

restaurant = Restaurant("the swiss hotel", "pizza")


# print(restaurant.name)
# print(restaurant.cusine_type)
        
restaurant.describe_restaurant()
restaurant.open_restaurant()
