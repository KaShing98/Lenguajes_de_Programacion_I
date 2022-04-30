from Class import Class

class VirtualMethodsSystem:
    def __init__(self):
        self.classes = {}

    def add_class(self, name, methods, super_class_name=None):
        """
        Agrega una clase al sistema si es valido, o si no esta en el sistema
        """
        self.check_candidate(name, methods, super_class_name)

        super_class = self.classes[super_class_name] if super_class_name is not None else None
        self.classes[name] = Class(name, methods, super_class)

    def check_candidate(self, name, methods, super_class_name=None):
        """
        Chequea si una clase cumple las condiciones, no es necesario chequear por loops por las otras validaciones
        """
        if len(name) > 0 and name in self.classes:
            raise Exception(f'La clase {name} ya se encuentra en el sistema.')

        if super_class_name is not None and super_class_name not in self.classes:
            raise Exception(f'La super clase {super_class_name} no se encuentra en el sistema.')

        if len(methods) != len(set(methods)):
            raise Exception(f'La declaración contiene métodos repetidos.')

    def describe(self, name, *args):
        """
        Describe una clase
        """
        if name not in self.classes:
            raise Exception(f'La clase {name} no se encuentra en el sistema.')

        return self.classes[name].print_methods()
    
