class AstNode:
    def __init__(self, parent=None):
        self.name = ""
        self.parent = parent
        self.children = []
        self.depth = 0

    def prepare_to_print(self):
        pass

    def c_visitor(self):
        pass
