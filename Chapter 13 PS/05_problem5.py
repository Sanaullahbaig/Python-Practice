from functools import reduce
l = [12, 56, 678, 987, 790, 50, 5, 2, 20, 25, 30, 678, 90]

def greater(a, b):
    if (a > b):
        return a
    return b
s = reduce(greater, l)
print(s)

# We can also write it using lambda
m = reduce(lambda a, b: a if a > b else b, l)
print(m)