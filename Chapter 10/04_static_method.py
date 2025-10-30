class Employe:
    language = "Python"
    salary = "100000" 

    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")

    @staticmethod # now greet is a static method it will not take self , it means we dont use any attribute of class
    def greet():
        print("hello")

harry = Employe()

harry.getInfo() 
harry.greet()
# Emplye.getInfo(harry) this is second method to call