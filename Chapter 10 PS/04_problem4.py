class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of number is: {self.n * self.n}")

    def cube(self):
        print(f"The cube of number is: {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square root of number is: {self.n ** (1/2)}")

    @staticmethod
    def greet():
        print("Hello!")

a = Calculator(9)
a.greet()
a.square()
a.cube()
a.square_root()
