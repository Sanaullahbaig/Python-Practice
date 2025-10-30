# super method called the cunstructor of parent class

class Employe:
    def __init__(self):
        print("This is the constructor of Employe.")
    a = 1

class Programmer(Employe):
    def __init__(self):
        super().__init__() # here super is used to call the parent class (Programmer) constructor
        print("This is the constructor of Programmer.")
    b = 2

class Manager(Programmer):
    def __init__(self):
      # super().function taht we want to call
        super().__init__() # here super() is used to call the parent class (Programmer) constructor
        print("This is the constructor of Manager.")
    c = 3

x = Manager()
print(x.a, x.b, x.c)