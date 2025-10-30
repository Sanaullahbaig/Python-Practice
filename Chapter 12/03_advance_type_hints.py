# Python typing modules provides more advance type hints such as List, Tuple, Dictionary and Union.
# Can import List, Tuple, Dict and Union types from the typing modules like this:
from typing import List, Tuple, Dict, Union

# List of integers
numbers : List[int] = [2, 43, 54, 65, 643, 5]

# Tuple of string and integer 
person : Tuple[str, int] = ("Ali", 43)

# Dictonary with key string and value integer 
score : Dict [str, int]= {"Ali" :50, "Ahmed" : 68, "Hassan" : 45}

identifier : Union [str, int] = "ID1233"
identifier = 12345 # Also valid 

print(type(numbers))
print(type(person))
print(type(score))
print(type(identifier))