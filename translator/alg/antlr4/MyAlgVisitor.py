# Generated from translator/alg/MyAlg.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyAlgParser import MyAlgParser
else:
    from MyAlgParser import MyAlgParser

# This class defines a complete generic visitor for a parse tree produced by MyAlgParser.

class MyAlgVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyAlgParser#program.
    def visitProgram(self, ctx: MyAlgParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)


    # Visit a parse tree produced by MyAlgParser#type.
    def visitType(self, ctx:MyAlgParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#type_basic.
    def visitType_basic(self, ctx:MyAlgParser.Type_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#statements.
    def visitStatements(self, ctx:MyAlgParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#statement.
    def visitStatement(self, ctx:MyAlgParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#ifElseSt.
    def visitIfElseSt(self, ctx:MyAlgParser.IfElseStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#ifSt.
    def visitIfSt(self, ctx:MyAlgParser.IfStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#forSt.
    def visitForSt(self, ctx:MyAlgParser.ForStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#whileSt.
    def visitWhileSt(self, ctx:MyAlgParser.WhileStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#elseSt.
    def visitElseSt(self, ctx:MyAlgParser.ElseStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#gotoSt.
    def visitGotoSt(self, ctx:MyAlgParser.GotoStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#function.
    def visitFunction(self, ctx:MyAlgParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#args.
    def visitArgs(self, ctx:MyAlgParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#arg.
    def visitArg(self, ctx:MyAlgParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#assignSt.
    def visitNewVar(self, ctx: MyAlgParser.NewVarContext):
        print(
            f'New var {ctx.type_().getText()} {ctx.assignSt().left_expr().ident().getText()} {ctx.assignSt().expr().getText()}')
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAlgParser#label.
    def visitLabel(self, ctx:MyAlgParser.LabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAlgParser#assignSt.
    def visitAssignSt(self, ctx: MyAlgParser.AssignStContext):
        print(
            f'Assign var {ctx.left_expr().getText()} {ctx.expr().getText()}')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAlgParser#left_expr.
    def visitLeft_expr(self, ctx:MyAlgParser.Left_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#expr.
    def visitExpr(self, ctx:MyAlgParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#ident.
    def visitIdent(self, ctx:MyAlgParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#pointer.
    def visitPointer(self, ctx:MyAlgParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyAlgParser#array_access.
    def visitArray_access(self, ctx:MyAlgParser.Array_accessContext):
        return self.visitChildren(ctx)

