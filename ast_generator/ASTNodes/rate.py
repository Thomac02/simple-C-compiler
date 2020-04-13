from .astnode import *


class Rate(AstNode):
    def __init__(self):
        super(Rate, self).__init__(parent=None)
        self.val = None

    def prepare_to_print(self):
        self.name += "Rate "