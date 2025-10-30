# This is a global value we can run it inside the function and also outhside function
a = 8

def fun():
    # global will change the value of a from 8 to 7
    global a
    a = 7
    print(a)

fun()
print(a)
