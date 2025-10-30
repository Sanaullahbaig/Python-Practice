f = open("file.txt")
data = f.read()
print(data)
f.close()

# The same can be written by using with statement like this:

with open("file.txt") as f:
    data = f.read()
    print(data)

# You don't have to explicity close the file as you close in the first code  