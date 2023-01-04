# Defining a Function
def greet_user():
    """Display a simple greeting."""
    print("Assalamu alaykum!")

greet_user()


# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Assalamu alaykum, {username.title()}!")

greet_user("success")
