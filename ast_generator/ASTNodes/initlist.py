from .astnode import *


class InitList(AstNode):
    def __init__(self):
        super(InitList, self).__init__(parent=None)
        self.expr = []

    def prepare_to_print(self):
        self.name += "InitList: "