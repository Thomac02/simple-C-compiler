from .astnode import *


class UnaryOperator(AstNode):
    def __init__(self):
        super(UnaryOperator, self).__init__(parent=None)
        self.op = None
        self.expr = None
        self.iscond = False

    def prepare_to_print(self):
        self.name += "UnaryOp: " + self.op + " "

    def c_visitor(self):
        return self.op + self.expr.to_string()