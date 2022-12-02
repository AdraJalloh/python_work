# Removing an Item Using the pop() Method:
motorcycles = ["ducati", "kawasaki", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I own is a {last_owned.title()}.")

# Popping Items from Any Position in a List
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I own was a {first_owned.title()}.")
