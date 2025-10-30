class Employe:
    salary = 55380
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + ((self.salary / 100) * self.increment)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/ self.salary) -1 ) * 100

e = Employe()
a = e.salaryAfterIncrement # As we use property method so we dont need to call salaryAfterIncrement as a function
print(a)
e.salaryAfterIncrement = 66456.0
print(e.increment)