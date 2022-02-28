from Memory import Memory

class BuddySystem:
    def __init__(self, size):
        self.memory = Memory(size)
        self.names = {}

    def Reservar(self, name, size):
        if name in self.names:
            return "Block under name {} was already reserved".format(name)

        if (isinstance(size,str)):
            size = int(size)

        status = self.memory.allocate(name, size)

        if status:
            self.names[name] = size
            return "Block under name {} was reserved".format(name)
        else:
            return "Block under name {} cannot be reserved".format(name)

        return status

    def Liberar(self, name):
        if name not in self.names:
            return "Block under name {} does not exists".format(name)

        status = self.memory.unallocate(name)

        if status:
            self.names.pop(name, None)
            return "Block under name {} was free".format(name)

        return status

    def Mostrar(self):
        return self.memory.print()
