# Clase para representar un bloque de memoria
class Block:
    def __init__(self, size, used=False, split=False):
        self.size = size
        self.used = used
        self.split = split
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_size(self):
        return self.size

    def get_split(self):
        return self.split

    def set_split(self, split):
        self.split = split

    def get_used(self):
        return self.used

    def set_used(self, used):
        self.used = used

# Clase para representar la memoria
class Memory:
    def __init__(self, size):
        # self.left y self.right son diferentes de null, si la memoria fue dividida
        self.left = None
        self.right = None
        # representacion del bloque actual
        self.val = Block(size)

    def split(self, size):
        # Funcion split: divide el bloque si el espacio a reservar es mas grande que la siguiente potencia

        actual_block_size = self.val.get_size()
        next_block_size = self.val.get_size() // 2

        if (next_block_size >= size and size < actual_block_size and not self.val.get_split()):
            self.val.set_split(True)
            # print(next_block_size)
            self.left = Memory(next_block_size)
            self.right = Memory(next_block_size)

    def allocate(self, name, size):
        # Funcion allocate: divide la memoria para conseguir el bloque más ajustado y asignarla
        # Retorna:
        #   True: si se asigno correctamente
        #   False: si no se asigno correctamente
        if self.val.get_used():
            return False

        # Si el bloque está libre, dividir si es posible para consegui el bloque más ajustado
        if (self.right is None and self.left is None and not self.val.get_used()):
            self.split(size)

        # Si se dividio, revisar si se puede asignar al bloque superior
        if (self.right is not None and not self.right.val.get_used()):
            status = self.right.allocate(name, size)
            if status:
                return status

        # Si se dividi0, y no fue asignado al bloque superior, revisar si se puede asignar al bloque inferior
        if (self.left is not None and not self.left.val.get_used()):
            status = self.left.allocate(name, size)
            if status:
                return status

        # Si no se dividio, entonces este es el bloque mas ajustado, ver si se puede asignar
        if (self.right is None and self.left is None):
            if (not self.val.get_used() and size <= self.val.get_size()):
                self.val.set_used(True)
                self.val.set_name(name)
                return True
            
        return False

    def unallocate(self, name):
        # Funcion unallocate: libera la memoria si fue ocupada
        # Retorna:
        #   True: si se libero correctamente
        #   False: si no se libero correctamente

        if (self.val.get_name() == name):
            self.val.set_used(False)
            self.val.set_name(None)

            if (self.left is not None and not self.left.val.get_used() and self.left.val.get_split()):
                self.left = None

            if (self.right is not None and not self.right.val.get_used() and self.right.val.get_split()):
                self.right = None

            if (self.right is None and self.left is None):
                self.val.set_split(False)

            return True
        else:
            if (self.right is not None):
                status = self.right.unallocate(name)
                if status:
                    return status

            if (self.left is not None):
                status = self.left.unallocate(name)
                if status:
                    return status

        return False

    def print(self):
        # Funcion print: imprime una representacion de la memoria
        # Recorre el arbol con una funcion similar a BFS
        visited = {}
        queue = []
 
        queue.append(self)
        visited[self.val.get_name()] = True

        text = ""
        while queue:
            s = queue.pop(0)
            
            name = s.val.get_name()
            if name is not None:
                text += "[USED] Name: {}, Size: {}\n".format(s.val.get_name(), s.val.get_size())
            else:
                if (s.val is not None and s.left is None and s.left is None):
                    text += "[FREE] Size: {}\n".format(s.val.get_size())

                if (s.val is not None and s.right is not None and s.right.val is not None):
                    queue.append(s.right)

                if (s.val is not None  and s.left is not None and s.left.val is not None):
                    queue.append(s.left)

        return text

