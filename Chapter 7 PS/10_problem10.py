n = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
    i -= 1

# second method 

for i in range(1, 11):
    print(f"{n} x {11 - i} = {n * (11 - i)}")
    i += 1