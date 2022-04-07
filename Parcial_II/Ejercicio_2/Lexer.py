import ply.lex as lex
from Constants import *

class Lexer:
    def __init__(self):

        def t_NUMBER(t):
            r'\d+'
            t.value = int(t.value)    
            return t
        
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)
        
        t_ignore  = ' \t'
        
        # Error handler
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)

        self.lexer = lex.lex()

    def getLexer(self):
        """
        Retorna analizador lexicografico
        """
        return self.lexer