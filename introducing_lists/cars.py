# Sorting a List Permanently with the sort() Method
# Alphabetical order:
cars = ["bmw", "audi", "toyota", "subaru", "tesla"]
cars.sort()
print(cars)

# Reverse-alphabetical order:
# cars = ["bmw", "audi", "toyota", "subaru", "tesla"]
cars.sort(reverse=True)
print(cars)
print("\n")


# Sorting a List Temporarily with the sorted() Function
cars = ["bmw", "audi", "toyota", "subaru", "tesla"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
print("\n")


# Printing a List in Reverse Order
cars = ["audi", "bmw", "subaru", "tesla", "toyota"]
print(cars)

cars.reverse()
print(cars)

