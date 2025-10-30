# Encapsulation means binding data (variables) and methods (functions) that operate on that data 
# into a single unit — a class — and restricting direct access to the data from outside the class.
# Here is the concept of encapsulation here we have written functions, methods in a single class


# Here is the concept of Abstraction hiding complexity 
# Abstraction means showing only the essential features 
# of an object and hiding the unnecessary details from the user.

class Employe:

    @property
    def name(self):  # proper make the function act like a variable not like function
        return f"{self.fname} {self.lname}"# it's a getter use to get the value of ename

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employe()

e.name = "Harry Khan"
print(e.name)
print(e.lname, e.fname)
