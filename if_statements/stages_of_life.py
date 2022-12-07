# Stages of Life
age = 66
if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else: 
    print("The person is an elder.")


# Revised code
age = 33
if age < 2:
    person = "a baby"
elif age >= 2 and age < 4:
    person = "a toddler"
elif age >= 4 and age < 13:
    person = "a kid"
elif age >= 13 and age < 20:
    person = "a teenager"
elif age >= 20 and age < 65:
    person = "an adult"
else: 
    person = "an elder"

print(f"The person is {person}.")