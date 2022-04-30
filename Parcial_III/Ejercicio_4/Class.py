
class Class:
    def __init__(self, name, methods, super_class=None):
        self.name = name
        self.methods = dict.fromkeys(methods, name)
        self.super_class = super_class

        if self.super_class is not None:
            self.methods = {**super_class.get_methods(), **self.methods}

    def get_methods(self):
        """
        Retorna los metodos de la clase 
        """
        return self.methods

    def print_methods(self):
        """
        Describe la clase 
        """
        methods = [f'{m} -> {self.methods[m]} :: {m}' for m in sorted([*self.methods])]
        return '\n'.join(methods)


