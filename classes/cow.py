class Cow:
    """A simple attempt to model a cow."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age 

    def sit(self):
        """Simulate a cow sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_cow = Cow('Adra', 6)
your_cow = Cow('Rizq', 3)

print(f"My cow's name is {my_cow.name}.")
print(f"My cow is {my_cow.age} years old.")
my_cow.sit()

print(f"\nYour cow's name is {your_cow.name}.")
print(f"Your cow is {your_cow.age} years old.")
your_cow.sit()
