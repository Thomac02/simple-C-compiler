# Generated from C:/Final Year/C Compiler/PyCharm projects/C\C.g4 by ANTLR 4.7.2
from antlr4 import *
from ast import *

if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser


# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):
    def __init__(self, ast):
        self.ast = ast

    # Helper functions
    # for assigning left and right of binaryop/assignment
    def assign_left_and_right(self, ASTNode):
        if isinstance(self.ast.currentnode, BinaryOp):
            if self.ast.currentnode.left is None:
                self.ast.currentnode.left = ASTNode
                self.ast.currentnode.children.append(ASTNode)
            else:
                self.ast.currentnode.right = ASTNode
                self.ast.currentnode.children.append(ASTNode)
        elif isinstance(self.ast.currentnode, Assignment):  # assignment - can i assume this?
            if self.ast.currentnode.lvalue is None:
                self.ast.currentnode.lvalue = ASTNode
                self.ast.currentnode.children.append(ASTNode)
            else:
                self.ast.currentnode.rvalue = ASTNode
                self.ast.currentnode.children.append(ASTNode)
        elif isinstance(self.ast.currentnode, Decl):  # for declaration initval
            self.ast.currentnode.initialval = ASTNode
        elif isinstance(self.ast.currentnode, Return):
            self.ast.currentnode.expr = ASTNode
            self.ast.currentnode.children.append(ASTNode)
            # do I need to update last node if i know that constants/identifiers wont have children?

    # Enter a parse tree produced by CParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: CParser.PrimaryExpressionContext):
        # this whole function needs to change, currently relies on previous node being binary op when it could
        # be assignment etc.
        if ctx.Constant() is not None:  # 'if X is not None' is faster than 'if X'
            constant = Constant()
            constant.value = ctx.children[0].getText()
            constant.depth = self.ast.currentnode.depth + 1;
            if constant.value.find("'") != -1:
                constant.type = "char"
            elif constant.value.find(".") != -1:
                constant.type = "float"
            else:
                constant.type = "int"
            self.assign_left_and_right(constant)
        elif ctx.Identifier() is not None:
            identifier = ID(ctx.children[0].getText())
            identifier.depth = self.ast.currentnode.depth + 1;
            self.assign_left_and_right(identifier)

    # Exit a parse tree produced by CParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: CParser.PrimaryExpressionContext):
        pass

    # Enter a parse tree produced by CParser#genericSelection.
    def enterGenericSelection(self, ctx: CParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by CParser#genericSelection.
    def exitGenericSelection(self, ctx: CParser.GenericSelectionContext):
        pass

    # Enter a parse tree produced by CParser#genericAssocList.
    def enterGenericAssocList(self, ctx: CParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by CParser#genericAssocList.
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
        pass

    # Exit a parse tree produced by CParser#postfixExpression.
    def exitPostfixExpression(self, ctx: CParser.PostfixExpressionContext):
        pass

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
        if ctx.Star() is not None:
            binaryOp.op = "*"
        elif ctx.Div() is not None:
            binaryOp.op = "/"
        elif ctx.Mod() is not None:
            binaryOp.op = "%"
        else:
            return
        binaryOp.depth = self.ast.currentnode.depth + 1
        self.ast.currentnode.children.append(binaryOp)
        binaryOp.parent = self.ast.currentnode
        self.ast.currentnode = binaryOp

    # Exit a parse tree produced by CParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx: CParser.MultiplicativeExpressionContext):
        if ctx.getChildCount() < 2:
            return
        self.ast.currentnode = self.ast.currentnode.parent

    # Enter a parse tree produced by CParser#additiveExpression.
    def enterAdditiveExpression(self, ctx: CParser.AdditiveExpressionContext):
        if ctx.getChildCount() < 2:
            return
        binaryOp = BinaryOp()
        if ctx.Plus() is not None:
            binaryOp.op = "+"
        elif ctx.Minus() is not None:
            binaryOp.op = "-"
        else:
            return
        binaryOp.depth = self.ast.currentnode.depth + 1
        self.ast.currentnode.children.append(binaryOp)
        binaryOp.parent = self.ast.currentnode
        self.ast.currentnode = binaryOp

    # Exit a parse tree produced by CParser#additiveExpression.
    def exitAdditiveExpression(self, ctx: CParser.AdditiveExpressionContext):
        if ctx.getChildCount() < 2:
            return
        self.ast.currentnode = self.ast.currentnode.parent

    # Enter a parse tree produced by CParser#shiftExpression.
    def enterShiftExpression(self, ctx: CParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by CParser#shiftExpression.
    def exitShiftExpression(self, ctx: CParser.ShiftExpressionContext):
        pass

    # Enter a parse tree produced by CParser#relationalExpression.
    def enterRelationalExpression(self, ctx: CParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by CParser#relationalExpression.
    def exitRelationalExpression(self, ctx: CParser.RelationalExpressionContext):
        pass

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
            self.ast.currentnode = treeroot
        #############################

        assignmentNode.depth = self.ast.currentnode.depth + 1
        self.ast.currentnode.children.append(assignmentNode)
        assignmentNode.parent = self.ast.currentnode
        self.ast.currentnode = assignmentNode

    # Exit a parse tree produced by CParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx: CParser.AssignmentExpressionContext):
        if ctx.getChildCount() < 2:
            return
        if isinstance(self.ast.currentnode.parent, Compound):
            self.ast.currentnode.parent.block_items.append(self.ast.currentnode)
        self.ast.currentnode = self.ast.currentnode.parent

    # Enter a parse tree produced by CParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx: CParser.AssignmentOperatorContext):
        if ctx.Assign() is not None:
            self.ast.currentnode.op = "="
        elif ctx.DivAssign() is not None:
            self.ast.currentnode.op = "/="
        elif ctx.ModAssign() is not None:
            self.ast.currentnode.op = "%="
        elif ctx.PlusAssign() is not None:
            self.ast.currentnode.op = "+="
        elif ctx.MinusAssign() is not None:
            self.ast.currentnode.op = "-="
        elif ctx.LeftShiftAssign() is not None:
            self.ast.currentnode.op = "<<="
        elif ctx.RightShiftAssign() is not None:
            self.ast.currentnode.op = ">>="
        elif ctx.AndAssign() is not None:
            self.ast.currentnode.op = "&="
        elif ctx.XorAssign() is not None:
            self.ast.currentnode.op = "^="
        elif ctx.OrAssign() is not None:
            self.ast.currentnode.op = "|="
        else:
            print("No sign")
            return

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
        declNode.depth = self.ast.currentnode.depth + 1
        self.ast.currentnode.children.append(declNode)
        declNode.parent = self.ast.currentnode
        self.ast.currentnode = declNode

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx: CParser.DeclarationContext):
        self.ast.currentnode = self.ast.currentnode.parent

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
        if getattr(self.ast.currentnode, "type", False) is not False:
            # getattr will return None as either the default or if the attribute has a none value
            if ctx.Bool():
                self.ast.currentnode.type = "bool"
            if ctx.Char():
                self.ast.currentnode.type = "char"
            if ctx.Double():
                self.ast.currentnode.type = "double"
            if ctx.Float():
                self.ast.currentnode.type = "float"
            if ctx.Int():
                self.ast.currentnode.type = "int"
            if ctx.Long():
                self.ast.currentnode.type = "long"
            if ctx.Short():
                self.ast.currentnode.type = "short"

    # Exit a parse tree produced by CParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx: CParser.TypeSpecifierContext):
        pass

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
        pass

    # Exit a parse tree produced by CParser#typeQualifier.
    def exitTypeQualifier(self, ctx: CParser.TypeQualifierContext):
        pass

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
        if getattr(self.ast.currentnode, "name", False) is not False:
            self.ast.currentnode.name = ctx.getText()

    # Exit a parse tree produced by CParser#directDeclarator.
    def exitDirectDeclarator(self, ctx: CParser.DirectDeclaratorContext):
        if ctx.getChildCount() > 1 and isinstance(self.ast.currentnode.parent, FuncDef):
            self.ast.currentnode = self.ast.currentnode.parent

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
        pass

    # Exit a parse tree produced by CParser#parameterList.
    def exitParameterList(self, ctx: CParser.ParameterListContext):
        pass

    # Enter a parse tree produced by CParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx: CParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx: CParser.ParameterDeclarationContext):
        pass

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
        pass

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
        compoundnode.depth = self.ast.currentnode.depth + 1
        self.ast.currentnode.children.append(compoundnode)  # need to think about the order of these and if it matters
        compoundnode.parent = self.ast.currentnode
        self.ast.currentnode = compoundnode

    # Exit a parse tree produced by CParser#compoundStatement.
    def exitCompoundStatement(self, ctx: CParser.CompoundStatementContext):
        if ctx.getChildCount() < 2:
            return
        #for node in self.ast.currentnode.block_items:
         #   self.ast.currentnode.children.append(node)
        self.ast.currentnode = self.ast.currentnode.parent

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
        pass

    # Exit a parse tree produced by CParser#selectionStatement.
    def exitSelectionStatement(self, ctx: CParser.SelectionStatementContext):
        pass

    # Enter a parse tree produced by CParser#iterationStatement.
    def enterIterationStatement(self, ctx: CParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CParser#iterationStatement.
    def exitIterationStatement(self, ctx: CParser.IterationStatementContext):
        pass

    # Enter a parse tree produced by CParser#forCondition.
    def enterForCondition(self, ctx: CParser.ForConditionContext):
        pass

    # Exit a parse tree produced by CParser#forCondition.
    def exitForCondition(self, ctx: CParser.ForConditionContext):
        pass

    # Enter a parse tree produced by CParser#forDeclaration.
    def enterForDeclaration(self, ctx: CParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by CParser#forDeclaration.
    def exitForDeclaration(self, ctx: CParser.ForDeclarationContext):
        pass

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
        jumpNode.depth = self.ast.currentnode.depth + 1
        self.ast.currentnode.children.append(jumpNode)
        jumpNode.parent = self.ast.currentnode
        self.ast.currentnode = jumpNode

    # Exit a parse tree produced by CParser#jumpStatement.
    def exitJumpStatement(self, ctx: CParser.JumpStatementContext):
        if ctx.getChildCount() < 2:
            return
        if isinstance(self.ast.currentnode.parent, Compound):
            self.ast.currentnode.parent.block_items.append(self.ast.currentnode)
        self.ast.currentnode = self.ast.currentnode.parent

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
            self.ast.currentnode = treeroot

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
        funcdef.depth = self.ast.currentnode.depth + 1
        # TODO: Make a helper function like "set_relationship" to set parent, child and depth
        funcdef.parent = self.ast.currentnode
        self.ast.currentnode.children.append(funcdef)
        decl = Decl()
        decl.depth = funcdef.depth + 1
        funcdef.children.append(decl)
        self.ast.currentnode = decl
        self.ast.currentnode.parent = funcdef

    # Exit a parse tree produced by CParser#functionDefinition.
    def exitFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        pass

    # Enter a parse tree produced by CParser#declarationList.
    def enterDeclarationList(self, ctx: CParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by CParser#declarationList.
    def exitDeclarationList(self, ctx: CParser.DeclarationListContext):
        pass
