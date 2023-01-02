guests = ["amkam", "dask", "terror", "timbo", "versace", "ridwan", "suljay"]
print(guests)

print(f"Hey guys, sorry to let you know that I can only invite two people for the dinner.")
print("\n")

amkam = guests.pop()
print(f"Hey {amkam.title()}, i'm sorry I can't invite you to the dinner, ope you'll understand.")

dask = guests.pop()
print(f"Hey {dask.title()}, i'm sorry I can't invite you to the dinner, ope you'll understand.")

terror = guests.pop()
print(f"Hey {terror.title()}, i'm sorry I can't invite you to the dinner, ope you'll understand.")

timbo = guests.pop()
print(f"Hey {timbo.title()}, i'm sorry I can't invite you to the dinner, ope you'll understand.")

versace = guests.pop()
print(f"Hey {versace.title()}, i'm sorry I can't invite you to the dinner, ope you'll understand.")

ridwan = f"Assalamu alaykum {guests[0].title()}, i'm please to inviting you to a dinner."
suljay = f"Assalamu alaykum {guests[1].title()}, i'm please to inviting you to a dinner."

print(ridwan)
print(suljay)

print(guests)
del guests[0]
del guests[-1]
print(guests)




