# class mehod bound to the class and not the object of the class 
# it use cls instead of self

class Employe:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")

e = Employe()
e.a = 6  # it will not change the value of a because of class method

e.show()
