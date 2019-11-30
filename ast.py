class AST:
    def __init__(self):
        self.root = None
        self.lastNode = self.root

    def hasRoot(self):
        return self.root is not None


# We need to give the AST data structure some idea of the current 'active' node, so we know what
# to add a child to in the listener

class ASTNode:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}


class ArrayDecl(ASTNode):
    pass


class ArrayRef(ASTNode):
    pass


class Assignment(ASTNode):
    pass


class BinaryOp(ASTNode):
    def __init__(self):
        self.op = None
        self.left = None
        self.right = None


class Break(ASTNode):
    pass


class Case(ASTNode):
    pass


class Cast(ASTNode):
    pass


class Compound(ASTNode):
    pass


class CompoundLiteral(ASTNode):
    pass


class Constant(ASTNode):
    def __init__(self):
        self.type = None
        self.value = None


class Continue(ASTNode):
    pass


class Decl(ASTNode):
    pass


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
    pass


class Goto(ASTNode):
    pass


class ID(ASTNode):
    pass


class IdentifierType(ASTNode):
    pass


class If(ASTNode):
    pass


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
        self.expr = expr


class Struct(ASTNode):
    pass


class StructRef(ASTNode):
    pass


class Switch(ASTNode):
    pass


class TernaryOp(ASTNode):
    pass


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
