n : int = 5
name : str = "Ali"
#          type    type    type              
def sum(a: int, b: int) -> int:
    return a + b
a = sum(3, 4)
print(a)

# Variable type hint
age : int = 25
# Function type hints
def greeting(name: str) -> str:
    return f"Hello {name}!"
# Usage 
print(greeting("Ahmed"))