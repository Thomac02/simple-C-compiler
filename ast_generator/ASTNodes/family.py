from .astnode import *


class Family(AstNode):
    def __init__(self):
        super(Family, self).__init__(parent=None)
        self.val = None

    def prepare_to_print(self):
        self.name += "Family: "