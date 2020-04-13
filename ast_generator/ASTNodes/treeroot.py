from .astnode import *


class TreeRoot(AstNode):
    def __init__(self):
        super(TreeRoot, self).__init__(parent=None)
        self.name = None
