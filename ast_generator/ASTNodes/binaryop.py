from .astnode import *


class BinaryOp(AstNode):
    def __init__(self):
        super(BinaryOp, self).__init__(parent=None)
        self.op = None
        self.left = None
        self.right = None
        self.iscond = False

    def prepare_to_print(self):
        if self.iscond:
            self.name += "Condition: "
        self.name += "BinaryOp " + str(self.op) + " "

    def c_visitor(self):
        return self.left.to_string() + " " + self.op + " " + self.right.to_string()
