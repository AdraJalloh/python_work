num = input("Enter two numbers: ")

#num1, num2 = num.split(" ")
num1= num.split(" ")[0]
num2 = num.split(" ")[1]


print(int(num1) + int(num2))
