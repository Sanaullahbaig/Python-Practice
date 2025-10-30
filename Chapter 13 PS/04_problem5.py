l = [12, 56, 678, 987, 790, 50, 5, 2, 20, 25, 30, 678, 90]

def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = filter(divisible5, l)
print(list(a))

# we can also write it using lambda
b = filter(lambda x : x%5 == 0, l) # here we can use x and n both 
print(list(b))