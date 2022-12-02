# Adding Elements to a List
# Appending Elements to the End of a List
motorcycles = ["ducati", "honda", "suzuki"]
print(motorcycles)

motorcycles.append("yamaha")
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For example,
# you can start with an empty list and then add items to the list using a series
# of append() calls. Using an empty list, let’s add the elements 'honda', 'suzuki',
# and 'yamaha' to the list:

motorcycles = []

motorcycles.append("honda")
motorcycles.append("suzuki")
motorcycles.append("yamaha")

print(motorcycles)
