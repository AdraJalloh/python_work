users = []

if users:
    for user in users:
        print(f"Hello {user}, would you like to see a status report?")
    print(f"\nHello {user.title()}, thank you for logging in again.")    
else:
    print("We need to find some users!")

