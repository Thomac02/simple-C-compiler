from .astnode import *


class For(AstNode):
    def __init__(self):
        super(For, self).__init__(parent=None)
        self.init = None
        self.cond = None
        self.iter = None
        self.statement = None

    def prepare_to_print(self):
        self.name += "For loop: "

    def c_visitor(self):
        return "for("