class Vector:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

v1 = Vector([98, 5, 8])
print(len(v1))
