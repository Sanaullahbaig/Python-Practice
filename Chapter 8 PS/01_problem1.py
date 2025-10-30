def greatest(a, b, c):
    if (a > b and a > c):
        return "a is the greatest number." 
    elif (b > a and b > c):
        return "b is the greatest number."
    elif (c > a and c > b):
        return "c is the greatest number."
    
a = 432
b = 234
c = 8765

print(greatest(a, b, c))