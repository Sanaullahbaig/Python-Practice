# c = ((f - 32)/ 9) * 5

def f_to_c(f):
    return ((f - 32)/ 9) * 5


f = int(input("Enter temprature in F: "))
c = f_to_c(f)
#        round function is used to round decimal value here it is rounded into 2 values
print(f"{round(c, 2)} °C")