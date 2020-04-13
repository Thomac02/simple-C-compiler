from .astnode import *


class Return(AstNode):
    def __init__(self, expr=None):
        super(Return, self).__init__(parent=None)
        self.expr = expr

    def prepare_to_print(self):
        self.name += "Return "