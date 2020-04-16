from ast_generator.ast import AST

from .ASTNodes.arraydeclaration import ArrayDeclaration
from .ASTNodes.arrayreference import ArrayReference
from .ASTNodes.assignment import Assignment
from .ASTNodes.binaryop import BinaryOp
from .ASTNodes.compound import Compound
from .ASTNodes.declaration import Declaration
from .ASTNodes.for_ import For
from .ASTNodes.initlist import InitList
from .ASTNodes.return_ import Return
from .ASTNodes.unaryoperator import UnaryOperator
from .ASTNodes.while_ import While


class CAST(AST):
    def __init__(self, _input):
        super(CAST, self).__init__(_input)
        self.arraydims = []
        self.c_lines = ""
        self.tab_counter = 0

    def hasRoot(self):
        return self.root is not None

    def set_node_relationship(self, child, parent=None, attribute=None, setcurrent=True):
        if parent is None:
            parent = self.current_node
        if attribute is not None:
            currentstate = getattr(parent, attribute, False)  # currentstate is either false or value of attribute
            if currentstate is not False:
                if currentstate is not None and not isinstance(currentstate, list) and currentstate in parent.children:
                    parent.children.remove(currentstate)  # overwriting for typedecl and arraydecl
                setattr(parent, attribute, child) if not isinstance(currentstate, list) else currentstate.append(child)
        child.depth = parent.depth + 1
        parent.children.append(child)
        child.parent = parent
        if setcurrent:
            self.current_node = child

    def assign_terminal_attributes(self, node):
        if isinstance(self.current_node, BinaryOp):
            if self.current_node.left is None:
                self.set_node_relationship(node, None, "left")
            else:
                self.set_node_relationship(node, None, "right")
        elif isinstance(self.current_node, Assignment):
            if self.current_node.lvalue is None:
                self.set_node_relationship(node, None, "lvalue")
            else:
                self.set_node_relationship(node, None, "rvalue")
        elif isinstance(self.current_node, Declaration):  # for declaration initval
            self.set_node_relationship(node, None, "initialval")
        elif isinstance(self.current_node, ArrayDeclaration):
            self.arraydims.append(node)
            self.set_node_relationship(node, None, "dim")  # set them here to be reversed later
        elif isinstance(self.current_node, ArrayReference):
            if self.current_node.id is None:
                self.set_node_relationship(node, None, "id")
            else:
                self.set_node_relationship(node, None, "index")
        elif isinstance(self.current_node, Return):
            self.set_node_relationship(node, None, "expr")
        elif isinstance(self.current_node, While):
            self.set_node_relationship(node, None, "condition")
        elif isinstance(self.current_node, InitList):
            self.set_node_relationship(node, None, "expr")
        elif isinstance(self.current_node, UnaryOperator):
            self.set_node_relationship(node, None, "expr")
        elif isinstance(self.current_node, Rate):
            self.set_node_relationship(node, None, "val")
        elif isinstance(self.current_node, Family):
            self.set_node_relationship(node, None, "val")

    def reverse_array_dims(self, node):
        index = 0
        while isinstance(node, ArrayDeclaration):
            self.set_node_relationship(self.arraydims[index], node, "dim", False)
            node = node.type
            index = index + 1

    def generate_c(self, node):
        if isinstance(node, Compound):
            self.tab_counter += 1
        line = node.c_visitor()
        if line is not None:
            self.c_lines += line
        for child in node.children:
            if isinstance(node, Compound):
                self.c_lines += "\t" * self.tab_counter
            self.generate_c(child)
        if isinstance(node, Compound):
            self.tab_counter -= 1
        self.c_lines += self.get_c_line_ending(node)

    def get_c_line_ending(self, node):
        ending = ""
        if isinstance(node, BinaryOp) or isinstance(node, UnaryOperator):
            if isinstance(node.parent, For):
                if node == node.parent.iter:
                    ending = ") {\n"
                elif node == node.parent.cond:
                    ending = "; "
            elif isinstance(node.parent, While):
                if node.iscond:
                    ending = ") {\n"
            else:
                ending = ";\n"
        elif isinstance(node, Declaration) or isinstance(node, Assignment):
            if isinstance(node.parent, For) and (node == node.parent.init or node == node.parent.cond):
                ending = "; "
            else:
                ending = ";\n"
        elif isinstance(node, While) or isinstance(node, For):
            ending = "}\n"
        return ending

    def prepare_tree_for_printing(self, node):
        if node is not None:
            node.prepare_to_print()
            for child in node.children:
                self.prepare_tree_for_printing(child)

    # Credit clemtoy - https://github.com/clemtoy/pptree
    def print_tree(self, current_node, childattr='children', nameattr='name', indent='', last='updown'):

        if hasattr(current_node, nameattr):
            name = lambda node: getattr(node, nameattr)
        else:
            name = lambda node: str(node)

        children = lambda node: getattr(node, childattr)
        nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1
        size_branch = {child: nb_children(child) for child in children(current_node)}

        """ Creation of balanced lists for "up" branch and "down" branch. """
        # up = sorted(children(current_node), key=lambda node: nb_children(node))
        up = children(current_node)  # sorted version got order wrong
        down = []
        while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
            down.insert(0, up.pop())

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

    def print_c(self):
        self.generate_c(self.body_node)
        print(self.c_lines)


# We need to give the AST data structure some idea of the current 'active' node, so we know what
# to add a child to in the listener

