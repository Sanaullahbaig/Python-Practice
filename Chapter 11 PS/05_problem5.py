class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
v1 = Vector(98, 5, 8)
v2 = Vector(18, 26, 57)
v3 = Vector(2, 4, 3) # Same dimension vectors 

print(v1 + v2) # Output: v1 + v2
print(v2 * v3) # Output: v2 * v3

print(v2 + v3) # Output: v2 + v3
print(v2 * v2) # Output: v2 * v2

