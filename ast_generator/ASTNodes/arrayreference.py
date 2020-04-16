from .astnode import AstNode


class ArrayReference(AstNode):
    def __init__(self):
        super(ArrayReference, self).__init__(parent=None)
        self.id = None
        self.index = None

    def prepare_to_print(self):
        self.name += "ArrayRef: "
