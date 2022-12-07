# A program that simulates how websites ensures that everyone has a unique username.

current_users = ["adra", "admin", "leon", "mahfuz", "mlj", "noel", "rizq"]

new_users = ["adra", "haja", "iye", "rai", "mlj"] 

for username in new_users:
    if username in current_users:
        print(f"Enter a new username.")
    else:
        print(f"{username.title()} is available.")
    
print("\nFinished ensuring users to have unique usernames.")


