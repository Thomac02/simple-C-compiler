class AST:
    def __init__(self, _input):
        self.root = None
        self.current_node = self.root
        self.input = _input
