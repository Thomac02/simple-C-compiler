class AST:
    def __init__(self, input):
        self.root = None
        self.currentnode = self.root
        self.input = input  # name of the program

    def hasRoot(self):
        return self.root is not None

    def printNodes(self, node):
        formatspace = "    "
        if node is not None:
            node.printNode()
            for child in node.children:
                print(formatspace * child.depth, end=' ')
                self.printNodes(child)
        else:
            return


# We need to give the AST data structure some idea of the current 'active' node, so we know what
# to add a child to in the listener

class ASTNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.depth = 0

    def printNode(self):
        pass


class ArrayDecl(ASTNode):
    pass


class ArrayRef(ASTNode):
    pass


class Assignment(ASTNode):
    def __init__(self):
        super(Assignment, self).__init__(parent=None)
        self.op = None
        self.lvalue = None
        self.rvalue = None

    def printNode(self):
        if isinstance(self.parent, If) and self.parent.iftrue == self:
            print("True?")
        elif isinstance(self.parent, If) and self.parent.iffalse == self:
            print("False?")
        print("Assignment " + str(self.op))


class BinaryOp(ASTNode):
    def __init__(self):
        super(BinaryOp, self).__init__(parent=None)
        self.op = None
        self.left = None
        self.right = None

    def printNode(self):
        if isinstance(self.parent, If) and self.parent.cond == self:
            print("Condition: ", end=" ")
        print("BinaryOp " + str(self.op))


class Break(ASTNode):
    pass


class Case(ASTNode):
    pass


class Cast(ASTNode):
    pass


class Compound(ASTNode):
    def __init__(self):
        super(Compound, self).__init__(parent=None)
        self.block_items = []

    def printNode(self):
        print("Compound statement:")


class CompoundLiteral(ASTNode):
    pass


class Constant(ASTNode):
    def __init__(self):
        super(Constant, self).__init__(parent=None)
        self.type = None
        self.value = None

    def printNode(self):
        print("Constant " + str(self.type) + " " + str(self.value))


class Continue(ASTNode):
    pass


class Decl(ASTNode):
    def __init__(self):
        super(Decl, self).__init__(parent=None)
        self.name = None
        self.quals = []  # e.g. const, volatile, static
        self.funcspec = []  # e.g. inline
        self.storage = []  # e.g. extern, register etc.
        self.type = None
        self.initialval = None

    def printNode(self):
        print("Declaration: " + str(self.type) + " " + str(self.name), end=" ")
        if self.initialval is not None:
            print(" = ", self.initialval.value)
        else:
            print("")


class DeclList(ASTNode):
    pass


class Default(ASTNode):
    pass


class DoWhile(ASTNode):
    pass


class EllipsisParam(ASTNode):
    pass


class EmptyStatement(ASTNode):
    pass


class Enum(ASTNode):
    pass


class Enumerator(ASTNode):
    pass


class EnumeratorList(ASTNode):
    pass


class ExprList(ASTNode):
    pass


class For(ASTNode):
    pass


class FuncCall(ASTNode):
    pass


class FuncDecl(ASTNode):
    pass


class FuncDef(ASTNode):
    def __init__(self):
        super(FuncDef, self).__init__(parent=None)
        self.decl = None
        self.param_decls = []
        self.body = None

    def printNode(self):
        print("Function def:")


class Goto(ASTNode):
    pass


class ID(ASTNode):
    def __init__(self, name):
        super(ID, self).__init__(parent=None)
        self.name = name

    def printNode(self):
        print("Identifier " + str(self.name))


class IdentifierType(ASTNode):
    pass


class If(ASTNode):
    def __init__(self):
        super(If, self).__init__(parent=None)
        self.cond = None
        self.iftrue = None
        self.iffalse = None

    def printNode(self):
        print("If")


class InitList(ASTNode):
    pass


class Label(ASTNode):
    pass


class NamedInitializer(ASTNode):
    pass


class ParamList(ASTNode):
    pass


class Ptrdecl(ASTNode):
    pass


class Return(ASTNode):
    def __init__(self, expr=None):
        super(Return, self).__init__(parent=None)
        self.expr = expr

    def printNode(self):
        print("Return")


class Struct(ASTNode):
    pass


class StructRef(ASTNode):
    pass


class Switch(ASTNode):
    pass


class TernaryOp(ASTNode):
    pass


class TreeRoot(ASTNode):
    def __init__(self):
        super(TreeRoot, self).__init__(parent=None)
        self.name = None

    def printNode(self):
        print(self.name)


class TypeDecl(ASTNode):
    pass


class Typedef(ASTNode):
    pass


class Typename(ASTNode):
    pass


class UnaryOp(ASTNode):
    pass


class Union(ASTNode):
    pass


class While(ASTNode):
    pass


class Pragma(ASTNode):
    pass
