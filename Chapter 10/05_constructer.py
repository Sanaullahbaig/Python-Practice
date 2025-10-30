class Employe:
    language = "Python"
    salary = "100000" 

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

        print("I am creating an object.") # this is a dunder method which is automatically called

    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")

    @staticmethod # now greet is a static method it will not take self , it means we dont use any attribute of class
    def greet():
        print("hello")

harry = Employe("Harry", 1230000, "Java")
print(harry.name, harry.salary, harry.language)

# harry.getInfo() 
# harry.greet()
# Emplye.getInfo(harry) this is second method to call   

# ali = Employe()