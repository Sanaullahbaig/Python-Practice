a = int(input("Enter your age: "))

# if statement no: 1, it is an independent if 
if (a % 2 == 0):
    print("a is an even number.")
# end of if statement no: 1

# if statement no: 2
if (a >= 18 and a <= 60):
    print("You are above the age of consent.")
elif (a < 0):
    print("You are entering invalid age.")
elif (a > 60):
    print("You are too old.")
elif (a == 0):
    print("You are entering 0 which is not a valid age.")
else:
    print("You are below the age of consent.")
# end of if statement no: 2


print("End of program.")