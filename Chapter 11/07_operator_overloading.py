class Number:

    def __init__(self, n):
        self.n = n

    def __add__(self, num): # add method 
        return self.n + num.n

    def __sub__(self, num): # subtraction method
        return self.n - num.n 

    def __mul__(self, num): # Mulriplication method
        return self.n * num.n
    
    def __truediv__(self, num): # Decimal Division
        return self.n / num.n
    
    def __floordiv__(self, num): # Integer Division
        return self.n // num.n
    
n = Number(10)
m = Number(5)

print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)