from .astnode import *


class TypeDecl(AstNode):
    def __init__(self):
        super(TypeDecl, self).__init__(parent=None)
        self.declname = None
        self.type = None

    def prepare_to_print(self):
        self.name += "TypeDecl: " + self.type