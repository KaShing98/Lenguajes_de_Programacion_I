import math

class Vector:
    def __init__(self, x, y, z) -> None:
        # Representacion de vector, son tres coordenadas
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        # Funcion para convertir el vector a string
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        # Funcion para hacer comparaciones de equivalencia vectores
        if (isinstance(other, Vector)):
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        return False

    def __add__(self, other):
        # Funcion que suma vectores si other es un vector, si es un número opera con la suma a cada coord
        if (isinstance(other, Vector)):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        if (isinstance(other, (int, float))):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        # Funcion que resta vectores si other es un vector, si es un número opera con la resta a cada coord
        if (isinstance(other, Vector)):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        if (isinstance(other, (int, float))):
            return Vector(self.x - other, self.y - other, self.z - other)
    
    def __mul__(self, other):
        # Funcion que producto cruz vectores si other es un vector, si es un número opera con el producto a cada coord
        if (isinstance(other, Vector)):
            return Vector(
                self.y * other.z - self.z * other.y, 
                self.z * other.x - self.x * other.z, 
                self.x * other.y - self.y * other.x
            )
        if (isinstance(other, (int, float))):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __mod__(self, other):
        # Funcion que producto punto vectores si other es un vector, si es un número opera con el modulo a cada coord
        if (isinstance(other, Vector)):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if (isinstance(other, (int, float))):
            return Vector(self.x % other, self.y % other, self.z % other)

    