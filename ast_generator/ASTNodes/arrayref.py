from .astnode import AstNode


class ArrayRef(AstNode):
    def __init__(self):
        super(ArrayRef, self).__init__(parent=None)
        self.id = None
        self.index = None

    def prepare_to_print(self):
        self.name += "ArrayRef: "
