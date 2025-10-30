class Employe:
    salary = "100000" # class attribute 
    language = "Python" # class attribute
    company = "Google" # class attribute

ali = Employe() 
ali.name = "Ali" # object attribute / instance attribute 
print(ali.name, ali.salary, ali.language, ali.company)

ahmed = Employe()
ahmed.name = "Ahmed" # object attribute / instance attribute 
print(ahmed.name, ahmed.language, ahmed.salary)

# here name is object attribute / instance attribute  and salary, language and compnay are class attribute
#  as they directing belong to the class
