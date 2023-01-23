class User:
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initial the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personal greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

adra = User("adra", "success", "a_success", "as@example.com", "freetown")
adra.describe_user()
adra.greet_user()

dask = User("dask", "sebastian", "d_kamara", "ds@example", "freetown")
dask.describe_user()
dask.greet_user()
