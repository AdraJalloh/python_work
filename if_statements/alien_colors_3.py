alien = "yellow"
if alien == "green":
    print("Green alien just earned 5 points.")
elif alien == "yellow":
    print("Yellow alien just earned 10 points.")
else:
    print("Red alien just earned 15 points.")

# VERSION 1
alien = "green"
if alien == "green":
    color = 5
elif alien == "yellow":
    color = 10
elif alien == "red":
    color = 15

print(f"\n{alien.title()} alien just earned {color} points.")
    

# VERSION 2
alien = "yellow"
if alien == "green":
    color = 5
elif alien == "yellow":
    color = 10
elif alien == "red":
    color = 15

print(f"\n{alien.title()} alien just earned {color} points.")


# VERSION 3
alien = "red"
if alien == "green":
    color = 5
elif alien == "yellow":
    color = 10
elif alien == "red":
    color = 15

print(f"\n{alien.title()} alien just earned {color} points.")
