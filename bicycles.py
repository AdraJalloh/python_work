bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
# The following asks for the bicycles at index 1 and index 3:
print(bicycles[1])
print(bicycles[3])

# Special syntax for accessing last element in a list:
print(bicycles[-1])
print(bicycles[-1].title())

# This convention extends to other negative index
# values as well. The index -2 returns the second item from the end of the list,
# the index -3 returns the third item from the end, and so forth.
print(bicycles[-2].title())
print(bicycles[-3].title())

# Using Individual Values from a List:
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)