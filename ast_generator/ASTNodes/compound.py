from .astnode import *


class Compound(AstNode):
    def __init__(self):
        super(Compound, self).__init__(parent=None)
        self.block_items = []

    def prepare_to_print(self):
        self.name += "Compound statement: "
