import math

class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        if (isinstance(other, Vector)):
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        return False

    def __add__(self, other):
        if (isinstance(other, Vector)):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if (isinstance(other, Vector)):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return Vector(self.x - other, self.y - other, self.z - other)
    
    def __mul__(self, other):
        if (isinstance(other, Vector)):
            return Vector(
                self.y * other.z - self.z * other.y, 
                self.z * other.x - self.x * other.z, 
                self.x * other.y - self.y * other.x
            )
        return Vector(self.x * other, self.y * other, self.z * other)

    def __mod__(self, other):
        if (isinstance(other, Vector)):
            return self.x * other.x + self.y * other.y + self.z * other.z
        return Vector(self.x % other, self.y % other, self.z % other)

    