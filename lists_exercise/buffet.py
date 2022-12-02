# Buffet: Adra's Restaurant
foods = ("soup", "chips", "fries", "shawarma", "sandwich")
print("Adra's Restaurant Menu:")
# Python rejects this change.
# foods[1] = "kebbeh"
for food in foods:
    print(food.title())

# This is rejected too.
# foods[1] = "kebbeh"

# Restaurant Menu
foods = ("soup", "chips", "fries", "shawarma", "sandwich")
print("\nToday's Menu:")
for food in foods:
    print(food.title())

# Restaurant New Menu.
foods = ("sandwich", "tea", "kebbeh", "fries", "shawarma")
print("\nMonday's Menu:")
for food in foods:
    print(food.title())
