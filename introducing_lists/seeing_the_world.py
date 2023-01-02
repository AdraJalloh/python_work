places = ["saudi arabia", "egypt", "england", "united states", "ethopia"]
print(places)

print(sorted(places))

print("\nHere is my original list:")
print(places)

print(sorted(places))

print("\nHere is the original list again:")
print(places)
print("\n")

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)


print(places[len(places)-1])
print(places[2:])
print(places[:2])

name = "jalloh"
print(name)
print(name[0])
print(name[-1] + name[0] + name[1:3])
