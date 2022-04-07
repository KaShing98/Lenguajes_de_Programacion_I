from Prefix import PrefixParser 
from Postfix import PostParser

class Parser:
    def __init__(self):
        self.preParser = (PrefixParser()).getParser()
        self.postParser = (PostParser()).getParser()
        
    def getParser(self, mode):
        """
        Retorna el parser correspondiente al modo
        """
        if mode == "PRE":
            return self.preParser
        if mode == "POST":
            return self.postParser

    def eval(self, mode, input):
        """
        Evalua el input en el modo especificado
        """
        parser = self.getParser(mode)
        ast = parser.parse(input)
        return ast.eval()
    
    def show(self, mode, input):
        """
        Imprime el input de forma in-fija
        """
        parser = self.getParser(mode)
        ast = parser.parse(input)
        return ast.reconstruct()