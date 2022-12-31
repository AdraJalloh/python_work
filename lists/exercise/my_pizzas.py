pizzas = ["cheese", "meat", "margherita", "pepperoni"]
friend_pizzas = pizzas[:]

pizzas.append("supreme")
friend_pizzas.append("veggie")

print("\nMy favorite pizzas are:")
for my_pizzas in pizzas:
    print(my_pizzas.title())

print("\nMy friend's favorite pizzas are:")
for your_pizzas in friend_pizzas:
    print(your_pizzas.title())   

