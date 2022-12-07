# Checking for Inequality
requested_toppings = "mushrooms"

if requested_toppings != "anchovies":
    print("Hold the anchovies!")

# Checking Whether a Value Is in a List
# requested_toppings = ["mushrooms", "onions", "pineapple"]
# "mushrooms" in requested_toppings

# "pepperoni" in requested_toppings

print("\n")

# Testing Multiple Conditions
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print("\nThis code would not work properly when we use an if-elif-else block, because the code stop running after only one test passes. Here’s what it looks like:\n")
print("-----------------------------")

# The code below would not work properly when using an if-elif-else block,
# because the code would stop running after only one test passes. 
# Here’s what it would look like:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("\n")
print("-----------------------------")

# Checking for Special Items
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_toppings in requested_toppings:
    print(f"Adding {requested_toppings}.")

print("\nFinished making your pizza!")


print("\n")
print("-----------------------------")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")


# Using Multiple Lists
print("\n#Using Multiple Lists:")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

