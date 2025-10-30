class Demo:
    a = 4

o = Demo()
print(o.a) # it prints class attribute as no instance attribute is present
o.a = 0 # Instance attribute is set
print(o.a) # Now it prints the instance attribute as it is present 

print(Demo.a) # instance attribute does not change the value of class attribute 