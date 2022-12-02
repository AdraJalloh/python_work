# Removing an Item by Value

motorcycles = ["ducati", "honda", "kawasaki", "suzuki", "yamaha"]
print(motorcycles)

motorcycles.remove("yamaha")
print(motorcycles)

# Let’s remove the value 'ducati' and print a reason for
# removing it from the list:

too_expensive = "kawasaki"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me.")