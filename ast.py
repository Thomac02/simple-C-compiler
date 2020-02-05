class AST:
    def __init__(self, input):
        self.root = None
        self.currentnode = self.root
        self.input = input  # name of the program

    def hasRoot(self):
        return self.root is not None

    def prepare_tree_for_printing(self, node):
        if node is not None:
            node.prepare_to_print()
            for child in node.children:
                self.prepare_tree_for_printing(child)

    # TESTING PRINT
    def print_tree(self, current_node, childattr='children', nameattr='name', indent='', last='updown'):

        if hasattr(current_node, nameattr):
            name = lambda node: getattr(node, nameattr)
        else:
            name = lambda node: str(node)

        children = lambda node: getattr(node, childattr)
        nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1
        size_branch = {child: nb_children(child) for child in children(current_node)}

        """ Creation of balanced lists for "up" branch and "down" branch. """
        up = sorted(children(current_node), key=lambda node: nb_children(node))
        down = []
        while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
            down.append(up.pop())

        """ Printing of "up" branch. """
        for child in up:
            next_last = 'up' if up.index(child) == 0 else ''
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', ' ' * len(name(current_node)))
            self.print_tree(child, childattr, nameattr, next_indent, next_last)

        """ Printing of current node. """
        if last == 'up':
            start_shape = '┌'
        elif last == 'down':
            start_shape = '└'
        elif last == 'updown':
            start_shape = ' '
        else:
            start_shape = '├'

        if up:
            end_shape = '┤'
        elif down:
            end_shape = '┐'
        else:
            end_shape = ''

        print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

        """ Printing of "down" branch. """
        for child in down:
            next_last = 'down' if down.index(child) is len(down) - 1 else ''
            next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', ' ' * len(name(current_node)))
            self.print_tree(child, childattr, nameattr, next_indent, next_last)


# We need to give the AST data structure some idea of the current 'active' node, so we know what
# to add a child to in the listener

class ASTNode:
    def __init__(self, parent=None):
        self.name = ""
        self.parent = parent
        self.children = []
        self.depth = 0

    def prepare_to_print(self):
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
        self.trueblock = False
        self.falseblock = False

    def prepare_to_print(self):
        if self.trueblock:
            self.name += "True? "
        elif self.falseblock:
            self.name += "False? "
        self.name += "Assignment " + str(self.op) + " "


class BinaryOp(ASTNode):
    def __init__(self):
        super(BinaryOp, self).__init__(parent=None)
        self.op = None
        self.left = None
        self.right = None
        self.iscond = False

    def prepare_to_print(self):
        if self.iscond:
            self.name += "Condition: "
        self.name += "BinaryOp " + str(self.op) + " "


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

    def prepare_to_print(self):
        self.name += "Compound statement: "


class CompoundLiteral(ASTNode):
    pass


class Constant(ASTNode):
    def __init__(self):
        super(Constant, self).__init__(parent=None)
        self.type = None
        self.value = None

    def prepare_to_print(self):
        self.name += "Constant " + str(self.type) + " " + str(self.value)


class Continue(ASTNode):
    pass


class Decl(ASTNode):
    def __init__(self):
        super(Decl, self).__init__(parent=None)
        self.quals = []  # e.g. const, volatile, static
        self.funcspec = []  # e.g. inline
        self.storage = []  # e.g. extern, register etc.
        self.type = None
        self.initialval = None

    def prepare_to_print(self):
        self.name = "Declaration: " + str(self.type) + " " + str(self.name)
        if self.initialval is not None:
            self.name += " = " + self.initialval.value


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

    def prepare_to_print(self):
        self.name += "Function def: " + self.decl.type + " " + self.decl.name


class Goto(ASTNode):
    pass


class ID(ASTNode):
    def __init__(self):
        super(ID, self).__init__(parent=None)

    def prepare_to_print(self):
        self.name = "Identifier " + self.name


class IdentifierType(ASTNode):
    pass


class If(ASTNode):
    def __init__(self):
        super(If, self).__init__(parent=None)
        self.cond = None
        self.iftrue = None
        self.iffalse = None

    def prepare_to_print(self):
        self.name += "If "


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

    def prepare_to_print(self):
        self.name += "Return "


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
