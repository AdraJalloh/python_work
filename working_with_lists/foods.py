# Copying a List
my_foods = ["pizza", "rice", "beans", "fish"]
friend_foods = my_foods[:]

# This doesn't work:
# friend_foods = my_foods

my_foods.append("meat")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

