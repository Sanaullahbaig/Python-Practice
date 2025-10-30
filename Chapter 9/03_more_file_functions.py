f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5)
# This will print nothing as there are just 5 line in txt file 
line6 = f.readline()
print(line6)

# we can also write it as 
line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()