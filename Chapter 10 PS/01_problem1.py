class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

a = Programmer("Ali", 100000, 592601)
print(a.name, a.salary, a.pincode, a.company)        

b = Programmer("Ahmed", 1200000, 956780)
print(b.name, b.salary, b.pincode, b.company)        