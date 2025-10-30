# inheritance is a way of creating a new class from an existing class 
# you can use the methods and attributes of parent class
# in child class

# class Employe: # Base class / parent class
#     code

# class Programmer(Employe): # Derived classs / child class
#     code


class Employe:
    company = "Petalnex"
    def show(self):
        print(f"The name of employe is {self.name} his salary is {self.salary}")

class Programmer(Employe):
    company = "Petalnex Tech"
    def showLanguage(self):
        print(f"The name of employe is {self.name} his salary is {self.salary} and he is good in {self.language} language")


a = Employe()
b = Programmer()
print(a.company, b.company)