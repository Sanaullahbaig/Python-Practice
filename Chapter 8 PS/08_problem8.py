def table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")

n = int(input("Enter a number: "))
table(n)