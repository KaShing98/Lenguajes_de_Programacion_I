import ply.yacc as yacc
from Lexer import Lexer
from Constants import *
from AST import *

class PostParser:
    def __init__(self):
        lexer = (Lexer()).getLexer()
        
        def p_expression_bin_op(p):
            """
            expression  : expression expression PLUS
                        | expression expression MINUS
                        | expression expression TIMES
                        | expression expression DIVIDE
            """
            p[0] = BinOp(p[1], p[3], p[2], prec[p[3]])

        def p_expression_num(p):
            """
            expression : NUMBER
            """
            p[0] = Num(p[1])
        
        def p_expression_expr(p):
            """
            expression : LPAREN expression RPAREN
            """
            p[0] = Parentheses(p[2])

        def p_error(p):
            print("Syntax error in input!")

        self.parser = yacc.yacc()

    def getParser(self):
        """
        Retorna parser para expresiones postfijas
        """
        return self.parser