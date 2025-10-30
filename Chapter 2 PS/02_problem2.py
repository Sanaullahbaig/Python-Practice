num1  = int(input("Enter first number: "))
num2  = int(input("Enter second number: "))
reminder = num1 % num2

if (num1 > num2):
    print(reminder)

elif (num1 < num2):
    print("For reminder first number should be greater then second number.")
else:
    print("Error!")