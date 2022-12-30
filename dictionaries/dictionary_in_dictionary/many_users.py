# A Dictionary in a Dictionary
users = {
    'asuccess': {
        'first': 'adra',
        'last': 'success',
        'location': 'freetown',
        },

    'qztiger': {
        'first': 'riqz',
        'last': 'tiger',
        'location': 'makeni',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
