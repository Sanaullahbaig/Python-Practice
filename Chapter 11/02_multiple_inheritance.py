# Inherit from more then one class / inerit from multiple classes

from random import randint

class Employe:
    company = "Petalnex"
    name = "Default name"

    def show(self):
        print(f"The name of employe is {self.name} and he works in company {self.company}")

class Coder():
    salary = randint(100000, 1000000)

    def showSalary(self):
        print(f"The name of employe is {self.name} and his salary is {self.salary}")

class Programmer(Employe, Coder): # multiple inheritance
    company = "Petalnex Tech"
    language = "Python"

    def showLanguage(self):
        print(f"The name of employe is {self.name} his salary is {self.salary} and he is good in {self.language} language and he works in company {self.company}")


a = Employe()
b = Programmer()

b.show()
b.showSalary()
b.showLanguage()
