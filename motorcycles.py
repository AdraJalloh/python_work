# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# To change an element, we use the name of the list followed
# by the index of the element that we want to change, and then provide the new
# value we want that item to have:
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List:
# Python provides several ways to add new data to any existing lists.
# 1. Appending Elements to the End of a List
motorcycles.append('kawasaki')
print(motorcycles)

# For example, starting out with an empty list and then add items to the list using a series of append() calls. And let’s add the elements 'honda', 'yamaha', 'suzuki'  and 'kawasaki' to the list:

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('kawasaki')

print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List:
# Removing an Item Using the del Statement.
del motorcycles[0]
print(motorcycles)

# Here’s how to remove the second item, 'yamaha', from the list:
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# We can use the pop() method to print a statement
# about the last motorcycle we bought:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

# Popping Items from Any Position in a List:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

