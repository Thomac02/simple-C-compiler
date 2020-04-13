from .astnode import *


class FuncDecl(AstNode):
    def __init__(self):
        super(FuncDecl, self).__init__(parent=None)
        self.args = None
        self.type = None

    def prepare_to_print(self):
        self.name += "FuncDecl: "

    def c_visitor(self):
        return "("
