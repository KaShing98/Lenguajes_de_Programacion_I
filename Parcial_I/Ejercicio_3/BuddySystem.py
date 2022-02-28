from Memory import Memory

# Clase para representar el Buddy System
class BuddySystem:
    def __init__(self, size):
        # Objeto para representar la memoria
        self.memory = Memory(size)
        # Tabla con los nombres de los espacios reservados
        self.names = {}

    def Reservar(self, name, size):
        # Función Reservar: permite reservar un espacio en memoria
        # Retorna: Sea a el nombre del espacio de memoria
        #   "Block under name a was already reserved" si ya hay un espacio con ese nombre
        #   "Block under name a was reserved" si el espacio fue reservado exitosamente
        #   "Block under name a cannot be reserved" si el espacio no pudo ser reservado

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
        # Función Liberar: permite liberar un espacio en memoria
        # Retorna: Sea a el nombre del espacio de memoria
        #   "Block under name a does not exists" si no hay un espacio con ese nombre
        #   "Block under name a was free" si el espacio fue liberado exitosamente
        if name not in self.names:
            return "Block under name {} does not exists".format(name)

        status = self.memory.unallocate(name)

        if status:
            self.names.pop(name, None)
            return "Block under name {} was free".format(name)

        return status

    def Mostrar(self):
        # Función Liberar: permite imprimir una representacion de la memoria
        return self.memory.print()
