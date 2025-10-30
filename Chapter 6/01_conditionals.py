a = int(input("Enter your age: "))

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

print("End of program.")