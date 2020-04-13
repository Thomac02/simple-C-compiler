import sys
from antlr4 import *
from ast_generator.CLexer import CLexer
from ast_generator.CParser import CParser
from ast_generator.CListener import CListener
from ast_generator.c_ast import CAST


def main(argv):
    # get input file from command line
    input = FileStream(argv[1])

    # lexer
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)

    # parser
    parser = CParser(stream)

    # parse tree
    tree = parser.translationUnit()

    # create the ast object, passing the name of the program to the constructor
    ast = CAST(argv[1])

    # create the listener and have it populate the ast
    clistener = CListener(ast)
    walker = ParseTreeWalker()
    walker.walk(clistener, tree)

    # print the ast
    ast.prepare_tree_for_printing(ast.root)
    ast.print_tree(ast.root)


if __name__ == '__main__':
    main(sys.argv)
