marks1 = int(input("Enter first subject marks: "))
marks2 = int(input("Enter second subject marks: "))
marks3 = int(input("Enter third subject marks: "))

# check for total percentage
total_percentage = ((marks1 + marks2 + marks3)/ 300) * 100

if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are passed.")
else:
    print("You are failed try again next year.")

