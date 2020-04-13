from .astnode import *


class Assignment(AstNode):
    def __init__(self):
        super(Assignment, self).__init__(parent=None)
        self.op = None
        self.lvalue = None
        self.rvalue = None
        self.trueblock = False
        self.falseblock = False

    def prepare_to_print(self):
        if self.trueblock:
            self.name += "True? "
        elif self.falseblock:
            self.name += "False? "
        self.name += "Assignment " + str(self.op) + " "

    def c_visitor(self):
        return self.lvalue.to_string() + " " + self.op + " " + self.rvalue.to_string()
