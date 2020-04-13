from .astnode import *


class Decl(AstNode):
    def __init__(self):
        super(Decl, self).__init__(parent=None)
        self.declname = None
        self.quals = []  # e.g. const, volatile, static
        self.funcspec = []  # e.g. inline
        self.storage = []  # e.g. extern, register etc.
        self.type = None
        self.initialval = None

    def prepare_to_print(self):
        self.name += "Declaration: " + str(self.declname) + " "

    def c_visitor(self):
        quals = ""
        initval = (" = " + self.initialval.to_string()) if self.initialval is not None else ""
        type = self.type
        while not isinstance(type, str):
            type = type.type
        for qual in self.quals:
            quals += qual.qual
        return quals + " " + type + " " + self.declname + initval