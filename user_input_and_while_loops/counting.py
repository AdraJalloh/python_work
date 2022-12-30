# The while Loop in Action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        
        continue
    # print(current_number)


# Avoiding Infinite Loops
# Every while loop needs a way to stop running so it won’t continue to run
# forever. For example, this counting loop should count from 1 to 5:
x = 1
while x <= 5:
    # print(x)
    x += 1

# However, if you accidentally omit the line x += 1, the loop will run forever:
# This loop runs forever!
x = 1
# while x <= 5:
    # print(x)
