class Employe:
    language = "Python"
    salary = "100000" 

    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")

    def greet(self):
        print("hello")
harry = Employe()

harry.getInfo() 
harry.greet()
# Emplye.getInfo(harry) this is second method to call