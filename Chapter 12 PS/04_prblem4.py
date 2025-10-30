try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    print(f"a / b = {a / b}")

except ZeroDivisionError as e:
    print("Infinite")