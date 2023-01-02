age = int(input("Please enter your age: "))

ages = []

while age < 5:
    ages.append(age)
    age = int(input("Enter age: "))

print(ages)