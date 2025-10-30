# when a child class become a parent class of another clind class
# Emoloye is a prent class, Coder is it's child 
# Proogrammer is a child class and inherit properties from both parent
#  (Employe) and another child class (Coder)

from random import randint

class Employe:
    company = "Petalnex"
    name = "Default name"

    def show(self):
        print(f"The name of employe is {self.name} and he works in company {self.company}")

class Coder(Employe):
    salary = randint(100000, 1000000)

    def showSalary(self):
        print(f"The name of employe is {self.name} and he works in company {self.company}, his salary is {self.salary}")

class Programmer(Coder):
    company = "Petalnex Tech"
    language = "Python"

    def showLanguage(self):
        print(f"The name of employe is {self.name} his salary is {self.salary} and he is good in {self.language} language and he works in company {self.company}")


a = Employe()
b = Programmer()

b.show()
b.showSalary()
b.showLanguage()
