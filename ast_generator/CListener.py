# Generated from AC.g4 by ANTLR 4.7
from antlr4 import *
from .ASTNodes.arraydecl import ArrayDecl
from .ASTNodes.arrayref import ArrayRef
from .ASTNodes.assignment import Assignment
from .ASTNodes.binaryop import BinaryOp
from .ASTNodes.compound import Compound
from .ASTNodes.constant import Constant
from .ASTNodes.decl import Decl
from .ASTNodes.for_ import For
from .ASTNodes.funcdecl import FuncDecl
from .ASTNodes.funcdef import FuncDef
from .ASTNodes.id import ID
from .ASTNodes.if_ import If
from .ASTNodes.initlist import InitList
from .ASTNodes.paramlist import ParamList
from .ASTNodes.rate import Rate
from .ASTNodes.return_ import Return
from .ASTNodes.treeroot import TreeRoot
from .ASTNodes.typedecl import TypeDecl
from .ASTNodes.typequal import TypeQual
from .ASTNodes.unaryop import UnaryOp
from .ASTNodes.while_ import While

if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser


# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):
    def __init__(self, ast):
        self.ast = ast

    # Enter a parse tree produced by CParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: CParser.PrimaryExpressionContext):
        # this whole function needs to change, currently relies on previous node being binary op when it could
        # be assignment etc.
        if ctx.Constant() is not None:  # 'if X is not None' is faster than 'if X'
            constant = Constant()
            constant.value = ctx.children[0].getText()
            if constant.value.find("'") != -1:
                constant.type = "char"
            elif constant.value.find(".") != -1:
                constant.type = "float"
            else:
                constant.type = "int"
            self.ast.assign_terminal_attributes(constant)
        elif ctx.Identifier() is not None:
            identifier = ID()
            identifier.name += ctx.getText()
            self.ast.assign_terminal_attributes(identifier)

    # Exit a parse tree produced by CParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: CParser.PrimaryExpressionContext):
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#genericSelection.
    def enterGenericSelection(self, ctx: CParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by CParser#genericSelection.
    def exitGenericSelection(self, ctx: CParser.GenericSelectionContext):
        pass

    # Enter a parse tree produced by CParser#genericAssocList.
    def enterGenericAssocList(self, ctx: CParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by CParser#genericAssocList.e
    def exitGenericAssocList(self, ctx: CParser.GenericAssocListContext):
        pass

    # Enter a parse tree produced by CParser#genericAssociation.
    def enterGenericAssociation(self, ctx: CParser.GenericAssociationContext):
        pass

    # Exit a parse tree produced by CParser#genericAssociation.
    def exitGenericAssociation(self, ctx: CParser.GenericAssociationContext):
        pass

    # Enter a parse tree produced by CParser#postfixExpression.
    def enterPostfixExpression(self, ctx: CParser.PostfixExpressionContext):
        if ctx.getChildCount() < 2:
            return
        if ctx.getChildCount() == 2:
            unaryop = UnaryOp()
            unaryop.op = ctx.children[1].getText()
            if isinstance(self.ast.current_node, While):
                unaryop.iscond = True;
            if isinstance(self.ast.current_node, For) and len(self.ast.current_node.children) == 2:
                self.ast.set_node_relationship(unaryop, None, "iter")
            else:
                self.ast.set_node_relationship(unaryop)
        else:
            arrayref = ArrayRef()
            self.ast.set_node_relationship(arrayref)

    # Exit a parse tree produced by CParser#postfixExpression.
    def exitPostfixExpression(self, ctx: CParser.PostfixExpressionContext):
        if ctx.getChildCount() < 2:
            return
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx: CParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by CParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx: CParser.ArgumentExpressionListContext):
        pass

    # Enter a parse tree produced by CParser#unaryExpression.
    def enterUnaryExpression(self, ctx: CParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CParser#unaryExpression.
    def exitUnaryExpression(self, ctx: CParser.UnaryExpressionContext):
        pass

    # Enter a parse tree produced by CParser#unaryOperator.
    def enterUnaryOperator(self, ctx: CParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CParser#unaryOperator.
    def exitUnaryOperator(self, ctx: CParser.UnaryOperatorContext):
        pass

    # Enter a parse tree produced by CParser#castExpression.
    def enterCastExpression(self, ctx: CParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by CParser#castExpression.
    def exitCastExpression(self, ctx: CParser.CastExpressionContext):
        pass

    # Enter a parse tree produced by CParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx: CParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() < 2:  # do i need this?
            return
        binaryOp = BinaryOp()
        binaryOp.op = ctx.children[1].getText()
        self.ast.set_node_relationship(binaryOp)

    # Exit a parse tree produced by CParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx: CParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() < 2:
            return
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#additiveExpression.
    def enterAdditiveExpression(self, ctx: CParser.AdditiveExpressionContext):
        if ctx.getChildCount() < 2:
            return
        binaryOp = BinaryOp()
        binaryOp.op = ctx.children[1].getText()
        self.ast.set_node_relationship(binaryOp)

    # Exit a parse tree produced by CParser#additiveExpression.
    def exitAdditiveExpression(self, ctx: CParser.AdditiveExpressionContext):
        if ctx.getChildCount() < 2:
            return
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#shiftExpression.
    def enterShiftExpression(self, ctx: CParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by CParser#shiftExpression.
    def exitShiftExpression(self, ctx: CParser.ShiftExpressionContext):
        pass

    # Enter a parse tree produced by CParser#relationalExpression.
    def enterRelationalExpression(self, ctx: CParser.RelationalExpressionContext):
        if ctx.getChildCount() < 2:
            return
        binaryOp = BinaryOp()
        binaryOp.op = ctx.children[1].getText()
        if isinstance(self.ast.current_node, If) or isinstance(self.ast.current_node, While):
            if self.ast.current_node.cond is None:  # TODO - check if set_relationship works for this
                binaryOp.iscond = True
        if isinstance(self.ast.current_node, For) and self.ast.current_node.cond is None:
            self.ast.set_node_relationship(binaryOp, None, "cond")
        else:
            self.ast.set_node_relationship(binaryOp)

    # Exit a parse tree produced by CParser#relationalExpression.
    def exitRelationalExpression(self, ctx: CParser.RelationalExpressionContext):
        if ctx.getChildCount() < 2:
            return

        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#equalityExpression.
    def enterEqualityExpression(self, ctx: CParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by CParser#equalityExpression.
    def exitEqualityExpression(self, ctx: CParser.EqualityExpressionContext):
        pass

    # Enter a parse tree produced by CParser#andExpression.
    def enterAndExpression(self, ctx: CParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CParser#andExpression.
    def exitAndExpression(self, ctx: CParser.AndExpressionContext):
        pass

    # Enter a parse tree produced by CParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx: CParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx: CParser.ExclusiveOrExpressionContext):
        pass

    # Enter a parse tree produced by CParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx: CParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx: CParser.InclusiveOrExpressionContext):
        pass

    # Enter a parse tree produced by CParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx: CParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by CParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx: CParser.LogicalAndExpressionContext):
        pass

    # Enter a parse tree produced by CParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx: CParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by CParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx: CParser.LogicalOrExpressionContext):
        pass

    # Enter a parse tree produced by CParser#conditionalExpression.
    def enterConditionalExpression(self, ctx: CParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by CParser#conditionalExpression.
    def exitConditionalExpression(self, ctx: CParser.ConditionalExpressionContext):
        pass

    # Enter a parse tree produced by CParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx: CParser.AssignmentExpressionContext):
        if ctx.getChildCount() < 2:
            return
        assignmentNode = Assignment()

        # TESTING - remove when done
        if not self.ast.hasRoot():
            treeroot = TreeRoot()
            self.ast.root = treeroot
            self.ast.current_node = treeroot
        #############################

        self.ast.set_node_relationship(assignmentNode)

    # Exit a parse tree produced by CParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx: CParser.AssignmentExpressionContext):
        if ctx.getChildCount() < 2:
            return
        if isinstance(self.ast.current_node.parent, Compound):
            self.ast.current_node.parent.block_items.append(self.ast.current_node)
        elif isinstance(self.ast.current_node.parent, If):
            if self.ast.current_node.parent.iftrue is None:
                self.ast.current_node.parent.iftrue = self.ast.current_node
                self.ast.current_node.trueblock = True
            elif self.ast.current_node.parent.iffalse is None:
                self.ast.current_node.parent.iffalse = self.ast.current_node
                self.ast.current_node.falseblock = True
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx: CParser.AssignmentOperatorContext):
        self.ast.current_node.op = ctx.getText()

    # Exit a parse tree produced by CParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx: CParser.AssignmentOperatorContext):
        pass

    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx: CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx: CParser.ExpressionContext):
        pass

    # Enter a parse tree produced by CParser#constantExpression.
    def enterConstantExpression(self, ctx: CParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CParser#constantExpression.
    def exitConstantExpression(self, ctx: CParser.ConstantExpressionContext):
        pass

    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx: CParser.DeclarationContext):
        declNode = Decl()
        self.ast.set_node_relationship(declNode)

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx: CParser.DeclarationContext):
        if not isinstance(self.ast.current_node, Decl):
            while not isinstance(self.ast.current_node, Decl):
                self.ast.current_node = self.ast.current_node.parent
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx: CParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by CParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx: CParser.DeclarationSpecifiersContext):
        pass

    # Enter a parse tree produced by CParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx: CParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by CParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx: CParser.DeclarationSpecifiers2Context):
        pass

    # Enter a parse tree produced by CParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx: CParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx: CParser.DeclarationSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx: CParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx: CParser.InitDeclaratorListContext):
        pass

    # Enter a parse tree produced by CParser#initDeclarator.
    def enterInitDeclarator(self, ctx: CParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#initDeclarator.
    def exitInitDeclarator(self, ctx: CParser.InitDeclaratorContext):
        pass

    # Enter a parse tree produced by CParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx: CParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx: CParser.StorageClassSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        if getattr(self.ast.current_node, "type", False) is not False:
            # getattr will return None as either the default or if the attribute has a none value
            typedecl = TypeDecl()
            typedecl.declname = self.ast.current_node.name
            self.ast.set_node_relationship(typedecl, None, "type")
            self.ast.current_node.type = ctx.getText()

    # Exit a parse tree produced by CParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx: CParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx: CParser.StructOrUnionSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#structOrUnion.
    def enterStructOrUnion(self, ctx: CParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by CParser#structOrUnion.
    def exitStructOrUnion(self, ctx: CParser.StructOrUnionContext):
        pass

    # Enter a parse tree produced by CParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx: CParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by CParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx: CParser.StructDeclarationListContext):
        pass

    # Enter a parse tree produced by CParser#structDeclaration.
    def enterStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#structDeclaration.
    def exitStructDeclaration(self, ctx: CParser.StructDeclarationContext):
        pass

    # Enter a parse tree produced by CParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx: CParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by CParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx: CParser.SpecifierQualifierListContext):
        pass

    # Enter a parse tree produced by CParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx: CParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by CParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx: CParser.StructDeclaratorListContext):
        pass

    # Enter a parse tree produced by CParser#structDeclarator.
    def enterStructDeclarator(self, ctx: CParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#structDeclarator.
    def exitStructDeclarator(self, ctx: CParser.StructDeclaratorContext):
        pass

    # Enter a parse tree produced by CParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx: CParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx: CParser.EnumSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#enumeratorList.
    def enterEnumeratorList(self, ctx: CParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by CParser#enumeratorList.
    def exitEnumeratorList(self, ctx: CParser.EnumeratorListContext):
        pass

    # Enter a parse tree produced by CParser#enumerator.
    def enterEnumerator(self, ctx: CParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by CParser#enumerator.
    def exitEnumerator(self, ctx: CParser.EnumeratorContext):
        pass

    # Enter a parse tree produced by CParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx: CParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by CParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx: CParser.EnumerationConstantContext):
        pass

    # Enter a parse tree produced by CParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx: CParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx: CParser.AtomicTypeSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#typeQualifier.
    def enterTypeQualifier(self, ctx: CParser.TypeQualifierContext):
        quals = {'const': 'const'}
        typeQual = TypeQual()
        typeQual.qual = quals[ctx.children[0].getText()]
        self.ast.set_node_relationship(typeQual, None, "quals")

    # Exit a parse tree produced by CParser#typeQualifier.
    def exitTypeQualifier(self, ctx: CParser.TypeQualifierContext):
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx: CParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx: CParser.FunctionSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx: CParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx: CParser.AlignmentSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#declarator.
    def enterDeclarator(self, ctx: CParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#declarator.
    def exitDeclarator(self, ctx: CParser.DeclaratorContext):
        pass

    # Enter a parse tree produced by CParser#directDeclarator.
    def enterDirectDeclarator(self, ctx: CParser.DirectDeclaratorContext):
        node = self.ast.current_node
        while getattr(node, "declname", False) is False:
            node = node.parent
        if ctx.Identifier() is not None:
            node.declname = ctx.getText()

        if ctx.getChildCount() > 1 and ctx.children[1].getText() == "[":
            arraydecl = ArrayDecl()
            arraydecl.type = self.ast.current_node.type
            self.ast.set_node_relationship(arraydecl.type, arraydecl, None, False)
            self.ast.set_node_relationship(arraydecl, None, "type")

            # TODO: Fix setting relationship in this case, I set the Decl type before (as child) and now overwriting it,
            # which means that although the type is now changed, the first TypeDecl is still a child of the Decl.
        elif ctx.getChildCount() > 1 and ctx.children[1].getText() == "(":
            funcdecl = FuncDecl()
            funcdecl.type = self.ast.current_node.type
            self.ast.set_node_relationship(funcdecl.type, funcdecl, None, False)
            self.ast.set_node_relationship(funcdecl, None, "type")
            print(self.ast.current_node)

    # Exit a parse tree produced by CParser#directDeclarator.
    def exitDirectDeclarator(self, ctx: CParser.DirectDeclaratorContext):
        if isinstance(self.ast.current_node, FuncDecl) and ctx.getChildCount() > 1:
            self.ast.current_node = self.ast.current_node.parent.parent
        elif isinstance(self.ast.current_node, ArrayDecl) and ctx.getChildCount() > 1:
            if not isinstance(self.ast.current_node.parent, ArrayDecl):
                self.ast.reverse_array_dims(self.ast.current_node)
            self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx: CParser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by CParser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx: CParser.GccDeclaratorExtensionContext):
        pass

    # Enter a parse tree produced by CParser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx: CParser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by CParser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx: CParser.GccAttributeSpecifierContext):
        pass

    # Enter a parse tree produced by CParser#gccAttributeList.
    def enterGccAttributeList(self, ctx: CParser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by CParser#gccAttributeList.
    def exitGccAttributeList(self, ctx: CParser.GccAttributeListContext):
        pass

    # Enter a parse tree produced by CParser#gccAttribute.
    def enterGccAttribute(self, ctx: CParser.GccAttributeContext):
        pass

    # Exit a parse tree produced by CParser#gccAttribute.
    def exitGccAttribute(self, ctx: CParser.GccAttributeContext):
        pass

    # Enter a parse tree produced by CParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx: CParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by CParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx: CParser.NestedParenthesesBlockContext):
        pass

    # Enter a parse tree produced by CParser#pointer.
    def enterPointer(self, ctx: CParser.PointerContext):
        pass

    # Exit a parse tree produced by CParser#pointer.
    def exitPointer(self, ctx: CParser.PointerContext):
        pass

    # Enter a parse tree produced by CParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx: CParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by CParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx: CParser.TypeQualifierListContext):
        pass

    # Enter a parse tree produced by CParser#parameterTypeList.
    def enterParameterTypeList(self, ctx: CParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by CParser#parameterTypeList.
    def exitParameterTypeList(self, ctx: CParser.ParameterTypeListContext):
        pass

    # Enter a parse tree produced by CParser#parameterList.
    def enterParameterList(self, ctx: CParser.ParameterListContext):
        if ctx.getChildCount() < 2:
            return
        if not isinstance(self.ast.current_node, ParamList):
            paramlist = ParamList()
            self.ast.set_node_relationship(paramlist)

    # Exit a parse tree produced by CParser#parameterList.
    def exitParameterList(self, ctx: CParser.ParameterListContext):
        if isinstance(ctx.parentCtx, CParser.ParameterListContext):
            return
        else:
            self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx: CParser.ParameterDeclarationContext):
        paramdecl = Decl()
        if isinstance(self.ast.current_node.parent, ParamList):
            self.ast.set_node_relationship(paramdecl, None, "params")
        else:
            self.ast.set_node_relationship(paramdecl)

    # Exit a parse tree produced by CParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx: CParser.ParameterDeclarationContext):
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#identifierList.
    def enterIdentifierList(self, ctx: CParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by CParser#identifierList.
    def exitIdentifierList(self, ctx: CParser.IdentifierListContext):
        pass

    # Enter a parse tree produced by CParser#typeName.
    def enterTypeName(self, ctx: CParser.TypeNameContext):
        pass

    # Exit a parse tree produced by CParser#typeName.
    def exitTypeName(self, ctx: CParser.TypeNameContext):
        pass

    # Enter a parse tree produced by CParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx: CParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx: CParser.AbstractDeclaratorContext):
        pass

    # Enter a parse tree produced by CParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx: CParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by CParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx: CParser.DirectAbstractDeclaratorContext):
        pass

    # Enter a parse tree produced by CParser#typedefName.
    def enterTypedefName(self, ctx: CParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CParser#typedefName.
    def exitTypedefName(self, ctx: CParser.TypedefNameContext):
        pass

    # Enter a parse tree produced by CParser#initializer.
    def enterInitializer(self, ctx: CParser.InitializerContext):
        pass

    # Exit a parse tree produced by CParser#initializer.
    def exitInitializer(self, ctx: CParser.InitializerContext):
        pass

    # Enter a parse tree produced by CParser#initializerList.
    def enterInitializerList(self, ctx: CParser.InitializerListContext):
        if isinstance(self.ast.current_node, InitList):
            return
        initlist = InitList()
        self.ast.set_node_relationship(initlist)

    # Exit a parse tree produced by CParser#initializerList.
    def exitInitializerList(self, ctx: CParser.InitializerListContext):
        pass

    # Enter a parse tree produced by CParser#designation.
    def enterDesignation(self, ctx: CParser.DesignationContext):
        pass

    # Exit a parse tree produced by CParser#designation.
    def exitDesignation(self, ctx: CParser.DesignationContext):
        pass

    # Enter a parse tree produced by CParser#designatorList.
    def enterDesignatorList(self, ctx: CParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by CParser#designatorList.
    def exitDesignatorList(self, ctx: CParser.DesignatorListContext):
        pass

    # Enter a parse tree produced by CParser#designator.
    def enterDesignator(self, ctx: CParser.DesignatorContext):
        pass

    # Exit a parse tree produced by CParser#designator.
    def exitDesignator(self, ctx: CParser.DesignatorContext):
        pass

    # Enter a parse tree produced by CParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx: CParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx: CParser.StaticAssertDeclarationContext):
        pass

    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx: CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx: CParser.StatementContext):
        pass

    # Enter a parse tree produced by CParser#labeledStatement.
    def enterLabeledStatement(self, ctx: CParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by CParser#labeledStatement.
    def exitLabeledStatement(self, ctx: CParser.LabeledStatementContext):
        pass

    # Enter a parse tree produced by CParser#compoundStatement.
    def enterCompoundStatement(self, ctx: CParser.CompoundStatementContext):
        compoundnode = Compound()
        self.ast.set_node_relationship(compoundnode)

    # Exit a parse tree produced by CParser#compoundStatement.
    def exitCompoundStatement(self, ctx: CParser.CompoundStatementContext):
        if ctx.getChildCount() < 2:
            return
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#blockItemList.
    def enterBlockItemList(self, ctx: CParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by CParser#blockItemList.
    def exitBlockItemList(self, ctx: CParser.BlockItemListContext):
        pass

    # Enter a parse tree produced by CParser#blockItem.
    def enterBlockItem(self, ctx: CParser.BlockItemContext):
        pass

    # Exit a parse tree produced by CParser#blockItem.
    def exitBlockItem(self, ctx: CParser.BlockItemContext):
        pass

    # Enter a parse tree produced by CParser#expressionStatement.
    def enterExpressionStatement(self, ctx: CParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CParser#expressionStatement.
    def exitExpressionStatement(self, ctx: CParser.ExpressionStatementContext):
        pass

    # Enter a parse tree produced by CParser#selectionStatement.
    def enterSelectionStatement(self, ctx: CParser.SelectionStatementContext):
        ifnode = If()
        self.ast.set_node_relationship(ifnode)

    # Exit a parse tree produced by CParser#selectionStatement.
    def exitSelectionStatement(self, ctx: CParser.SelectionStatementContext):
        if ctx.getChildCount() < 2:
            return
        # TODO can I do this with set_relationship now?
        if isinstance(self.ast.current_node.parent, If):
            if self.ast.current_node.parent.iftrue is None:
                self.ast.current_node.parent.iftrue = self.ast.current_node
            else:
                self.ast.current_node.parent.iffalse = self.ast.current_node
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#iterationStatement.
    def enterIterationStatement(self, ctx: CParser.IterationStatementContext):
        if ctx.For() is not None:
            fornode = For()
            self.ast.set_node_relationship(fornode)
        elif ctx.While() is not None:
            whilenode = While()
            self.ast.set_node_relationship(whilenode)
        else:
            dowhile = DoWhile()
            self.ast.set_node_relationship(dowhile)

    # Exit a parse tree produced by CParser#iterationStatement.
    def exitIterationStatement(self, ctx: CParser.IterationStatementContext):
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#forCondition.
    def enterForCondition(self, ctx: CParser.ForConditionContext):
        pass

    # Exit a parse tree produced by CParser#forCondition.
    def exitForCondition(self, ctx: CParser.ForConditionContext):
        pass

    # Enter a parse tree produced by CParser#forDeclaration.
    def enterForDeclaration(self, ctx: CParser.ForDeclarationContext):
        fordecl = Decl()
        self.ast.set_node_relationship(fordecl, None, "init")

    # Exit a parse tree produced by CParser#forDeclaration.
    def exitForDeclaration(self, ctx: CParser.ForDeclarationContext):
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#forExpression.
    def enterForExpression(self, ctx: CParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by CParser#forExpression.
    def exitForExpression(self, ctx: CParser.ForExpressionContext):
        pass

    # Enter a parse tree produced by CParser#jumpStatement.
    def enterJumpStatement(self, ctx: CParser.JumpStatementContext):
        if ctx.Return():
            jumpNode = Return()
        self.ast.set_node_relationship(jumpNode)

    # Exit a parse tree produced by CParser#jumpStatement.
    def exitJumpStatement(self, ctx: CParser.JumpStatementContext):
        if ctx.getChildCount() < 2:
            return
        if isinstance(self.ast.current_node.parent, Compound):
            self.ast.current_node.parent.block_items.append(self.ast.current_node)
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#compilationUnit.
    def enterCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CParser#compilationUnit.
    def exitCompilationUnit(self, ctx: CParser.CompilationUnitContext):
        pass

    # Enter a parse tree produced by CParser#translationUnit.
    def enterTranslationUnit(self, ctx: CParser.TranslationUnitContext):
        if not self.ast.hasRoot():
            treeroot = TreeRoot()
            treeroot.name = self.ast.input
            self.ast.root = treeroot
            self.ast.current_node = treeroot

    # Exit a parse tree produced by CParser#translationUnit.
    def exitTranslationUnit(self, ctx: CParser.TranslationUnitContext):
        pass

    # Enter a parse tree produced by CParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx: CParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx: CParser.ExternalDeclarationContext):
        pass

    # Enter a parse tree produced by CParser#functionDefinition.
    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        funcdef = FuncDef()
        self.ast.set_node_relationship(funcdef)
        decl = Decl()
        funcdef.decl = decl
        self.ast.set_node_relationship(decl, funcdef)

    # Exit a parse tree produced by CParser#functionDefinition.
    def exitFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        if ctx.getChildCount() < 2:
            return
        # self.ast.current_node.children.pop(0)
        self.ast.current_node = self.ast.current_node.parent

    # Enter a parse tree produced by CParser#declarationList.
    def enterDeclarationList(self, ctx: CParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by CParser#declarationList.
    def exitDeclarationList(self, ctx: CParser.DeclarationListContext):
        pass
