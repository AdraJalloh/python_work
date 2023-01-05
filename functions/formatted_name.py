# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jung', 'kook')
print(musician)

musician = get_formatted_name('fahad', 'kubaisi', 'al')
print(musician)
