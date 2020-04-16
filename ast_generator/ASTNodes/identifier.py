from .astnode import *


class Identifier(AstNode):
    def __init__(self):
        super(Identifier, self).__init__(parent=None)

    def prepare_to_print(self):
        self.name = "Identifier " + self.name

    def to_string(self):
        return self.name