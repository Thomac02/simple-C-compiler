from .astnode import *


class While(AstNode):
    def __init__(self):
        super(While, self).__init__(parent=None)
        self.cond = None
        self.body = None

    def prepare_to_print(self):
        self.name += "While: "
        # self.condition.name += "Condition: "
        # self.body.name += "Body: "

    def c_visitor(self):
        return "while("