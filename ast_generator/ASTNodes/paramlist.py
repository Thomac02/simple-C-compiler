from .astnode import *


class ParamList(AstNode):
    def __init__(self):
        super(ParamList, self).__init__(parent=None)
        self.params = []

    def prepare_to_print(self):
        self.name += "ParamList: "