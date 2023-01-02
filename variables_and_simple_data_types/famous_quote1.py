import random
import math
author_name= "Ibn Mas'ud"

# Step 1: List of Quotes
quotes = ["I love python", 'Programming is Life', 'Web development is the way',
        "I am from Maknei", "I started learning Java", "Mobile App",
        "Programming is better", "Test 1", "Test 2", "Test 3"]

# Step 2: Generate the quote
quote = round(random.random()*10)
print(quote)
#print(quotes[quote])
print(f'{quotes[quote]}')