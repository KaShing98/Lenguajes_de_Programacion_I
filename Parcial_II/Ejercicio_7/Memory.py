
class Tombstone:
    def __init__(self):
        self.tombstone = {}
        self.tombstone["Value"] = None
    
    def __str__(self):
        """
        Representacion en forma de string del valor que referencia el tombstone
        """
        return self.tombstone["Value"].__str__()

    def addValue(self, value):
        """
        Asigna una referencia a un valor a un tombstone
        """
        self.tombstone["Value"] = value
        return self

    def free(self):
        """
        Borra la referencia del tombstone y lo sustituye por un valor default
        """
        self.tombstone["Value"] = None

    def hasValue(self):
        """
        Retorna si el tombstone posee una referencia a un valor
        """
        return self.tombstone["Value"] is not None

class Memory:
    def __init__(self):
        self.memory = {}

    def inMemory(self, name, display=True):
        """
        Retorna si un valor esta asignado en memoria
        """
        if name in self.memory:
            return True
            
        if display:
            print("Not declared: {}".format(name))
        return False

    def reservar(self, name, value):
        """
        Reserva un espacio en memoria y asigna un valor
        """
        if not self.inMemory(name, False):
            ts = Tombstone()
            self.memory[name] = ts.addValue(value)
        else:
            self.memory[name].addValue(value)

    def asignar(self, nameA, nameB):
        """
        Asigna nameB a nameA
        """
        notDeclared = [name for name in [nameA, nameB] if name not in self.memory]
        if len(notDeclared) > 0:
            print("Not declared: {}".format(', '.join(notDeclared)))
            return

        self.memory[nameA] = self.memory[nameB]

    def liberar(self, name):
        """
        Libera el especio de memoria
        """
        if not self.inMemory(name):
            return
        
        self.memory[name].free()

    def imprimir(self, name):
        """
        Muestra el valor asignado a un espacio de memoria
        """
        if not self.inMemory(name):
            return

        if not self.memory[name].hasValue():
            print("{} has no value associated".format(name))
            return 

        print("Asociated value to {} is {}".format(name, self.memory[name]))