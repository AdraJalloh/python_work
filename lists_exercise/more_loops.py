my_foods = ["pizza", "rice", "beans", "fish"]
friend_foods = my_foods[:]

my_foods.append("meat")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())

