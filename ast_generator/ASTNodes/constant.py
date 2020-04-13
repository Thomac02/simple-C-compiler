from .astnode import *


class Constant(AstNode):
    def __init__(self):
        super(Constant, self).__init__(parent=None)
        self.type = None
        self.value = None

    def prepare_to_print(self):
        self.name += "Constant " + str(self.type) + " " + str(self.value)

    def to_string(self):
        return self.value
