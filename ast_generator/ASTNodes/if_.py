from .astnode import *


class If(AstNode):
    def __init__(self):
        super(If, self).__init__(parent=None)
        self.cond = None
        self.iftrue = None
        self.iffalse = None

    def prepare_to_print(self):
        self.name += "If "