a = (1,2,3,4,5)
print(type(a))

b = ()  # empty tuple
c = (1, ) # tuple with one element has a comma
d = (1, 6, 3, False, "Ali", 6, "Ahmed")
# d[0] = 45 tuple can't be changed 
print(d)
# count is used to count the items 
print(d.count(1))

# index method gives the first index of the value
print(d.index(6))

# len is used for the length
print(len(a))