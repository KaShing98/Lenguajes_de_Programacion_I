
class Types:
    def __init__(self):
        self.types = {}
        self.requiredArgs = {
            'atomic': 3,
            'struct': 2,
            'array': 3
        }
    
    def exists(self, name):
        return name in self.types

    def __validateValues(self, requiredArgs, args):
        if len(args) != requiredArgs:
            print("Number of arguments does not match")
            return False

        if self.exists(args[0]):
            print("Type of name {} already exists".format(args[0]))
            return False
        
        return True

    def addAtomic(self, input):
        args = input.split(" ")
        if (not self.__validateValues(self.requiredArgs['atomic'], args)):
            return 

        try:
            newAtom = Atomic(args[0], int(args[1]), int(args[2]))
            self.types[args[0]] = newAtom
        except ValueError:
            print("Type value error")

    def addStruct(self, input):
        args = input.split(" ")
        if (not self.__validateValues(self.requiredArgs['struct'], args[0:2])):
            return 

        notDefined = [type for type in args[1:] if type not in self.types]
        if (len(notDefined) == 0):
            types = [self.types[type] for type in args[1:]]
            newStruct = Struct(args[0], types)
            self.types[args[0]] = newStruct
        else:
            print("Not defined types: {}".format(', '.join(notDefined)))

    def addArray(self, input):
        args = input.split(" ")
        if (not self.__validateValues(self.requiredArgs['array'], args)):
            return 

        if (args[1] not in self.types):
            print("Not defined type: {}".format(args[1]))
            return 

        try:
            newArray = Array(args[0], args[1], int(args[2]))
            self.types[args[0]] = newArray
        except ValueError:
            print("Type value error")

    def describe(self, input):
        print("Not implemented") 


class Atomic:
    def __init__(self, name, bytes, alignment):
        self.name = name
        self.bytes = bytes
        self.alignment = alignment

class Struct:
    def __init__(self, name, types):
        self.name = name
        self.types = types

class Array:
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size

class Description:
    def __init__(self, packed_size, packed_loss, no_packed_size, no_packed_loss, optimum_size, optimum_loss):
        self.packed_size = packed_size
        self.packed_loss = packed_loss
        self.no_packed_size = no_packed_size
        self.no_packed_loss = no_packed_loss
        self.optimum_size = optimum_size
        self.optimum_loss = optimum_loss