stack = []

def push(x):
    stack.append(x)

push(3)

names = []

again = "y"


while again == "y":

    name = input("Enter your name: ")

    names.append(name)
    print(names)
    
    again = input('y = yes, anything else = no: ')
    