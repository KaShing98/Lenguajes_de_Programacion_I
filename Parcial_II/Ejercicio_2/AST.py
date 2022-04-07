import operator

class Node:
    def __str__(self):
        """
        Retorna la representacion en string del nodo
        """
        return self.reconstruct()

    def reconstruct(self):
        """
        Retorna la representacion en string del nodo en modo in-fijo
        """
        raise Exception("reconstruct is not defined in class " + self.__class__.__name__)

    def eval(self):
        """
        Evalua la expresion 
        """
        raise NotImplementedError("eval is not defined in class " + self.__class__.__name__)

class Num(Node):
    def __init__(self, expression):
        self.expr = expression

    def reconstruct(self):
        return "{}".format(self.expr)

    def eval(self):
        return int(self.expr)

class BinOp(Node):
    def __init__(self, l_expr, operator, r_expr, op_prec):
        self.l_expr = l_expr
        self.op = operator
        self.r_expr = r_expr
        self.op_prec = op_prec

    def reconstruct(self):
        l_expr = self.l_expr.reconstruct()
        r_expr = self.r_expr.reconstruct()

        if (isinstance(self.l_expr, BinOp) and self.l_expr.op_prec < self.op_prec):
            l_expr = "(" + l_expr + ")"

        if (isinstance(self.r_expr, BinOp) and self.r_expr.op_prec < self.op_prec):
            r_expr = "(" + r_expr + ")"
            
        return "{} {} {}".format(l_expr, self.op, r_expr)

    def eval(self):
        return {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }[self.op](self.l_expr.eval(), self.r_expr.eval())

class Parentheses(Node):
    def __init__(self, expression):
        self.expr = expression

    def reconstruct(self):
        return "({})".format(self.expr)

    def eval(self):
        return self.expr.eval()