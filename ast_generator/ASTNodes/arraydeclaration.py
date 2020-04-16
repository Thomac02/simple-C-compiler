from .astnode import AstNode


class ArrayDeclaration(AstNode):
    def __init__(self):
        super(ArrayDeclaration, self).__init__(parent=None)
        self.type = None
        self.dim = None
        self.dim_quals = None

    def prepare_to_print(self):
        self.name += "ArrayDecl: "

    def c_visitor(self):
        return "[" + self.dim.to_string() + "]"
