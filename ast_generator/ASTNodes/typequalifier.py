from .astnode import *


class TypeQualifier(AstNode):
    def __init__(self):
        super(TypeQualifier, self).__init__(parent=None)
        self.qual = None
        self.fam = None
        self.rate = None

    def prepare_to_print(self):
        self.name += "Type qualifier: " + self.qual + " "