from .astnode import *


class FuncDefinition(AstNode):
    def __init__(self):
        super(FuncDefinition, self).__init__(parent=None)
        self.decl = None
        self.param_decls = []
        self.body = None

    def prepare_to_print(self):
        self.name += "Function def: "