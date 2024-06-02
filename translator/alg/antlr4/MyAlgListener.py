# Generated from translator/alg/MyAlg.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyAlgParser import MyAlgParser
else:
    from MyAlgParser import MyAlgParser

# This class defines a complete listener for a parse tree produced by MyAlgParser.
class MyAlgListener(ParseTreeListener):

    # Enter a parse tree produced by MyAlgParser#program.
    def enterProgram(self, ctx:MyAlgParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyAlgParser#program.
    def exitProgram(self, ctx:MyAlgParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyAlgParser#type.
    def enterType(self, ctx:MyAlgParser.TypeContext):
        pass

    # Exit a parse tree produced by MyAlgParser#type.
    def exitType(self, ctx:MyAlgParser.TypeContext):
        pass


    # Enter a parse tree produced by MyAlgParser#type_basic.
    def enterType_basic(self, ctx:MyAlgParser.Type_basicContext):
        pass

    # Exit a parse tree produced by MyAlgParser#type_basic.
    def exitType_basic(self, ctx:MyAlgParser.Type_basicContext):
        pass


    # Enter a parse tree produced by MyAlgParser#statements.
    def enterStatements(self, ctx:MyAlgParser.StatementsContext):
        pass

    # Exit a parse tree produced by MyAlgParser#statements.
    def exitStatements(self, ctx:MyAlgParser.StatementsContext):
        pass


    # Enter a parse tree produced by MyAlgParser#statement.
    def enterStatement(self, ctx:MyAlgParser.StatementContext):
        pass

    # Exit a parse tree produced by MyAlgParser#statement.
    def exitStatement(self, ctx:MyAlgParser.StatementContext):
        pass


    # Enter a parse tree produced by MyAlgParser#ifElseSt.
    def enterIfElseSt(self, ctx:MyAlgParser.IfElseStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#ifElseSt.
    def exitIfElseSt(self, ctx:MyAlgParser.IfElseStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#ifSt.
    def enterIfSt(self, ctx:MyAlgParser.IfStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#ifSt.
    def exitIfSt(self, ctx:MyAlgParser.IfStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#forSt.
    def enterForSt(self, ctx:MyAlgParser.ForStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#forSt.
    def exitForSt(self, ctx:MyAlgParser.ForStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#whileSt.
    def enterWhileSt(self, ctx:MyAlgParser.WhileStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#whileSt.
    def exitWhileSt(self, ctx:MyAlgParser.WhileStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#elseSt.
    def enterElseSt(self, ctx:MyAlgParser.ElseStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#elseSt.
    def exitElseSt(self, ctx:MyAlgParser.ElseStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#gotoSt.
    def enterGotoSt(self, ctx:MyAlgParser.GotoStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#gotoSt.
    def exitGotoSt(self, ctx:MyAlgParser.GotoStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#function.
    def enterFunction(self, ctx:MyAlgParser.FunctionContext):
        pass

    # Exit a parse tree produced by MyAlgParser#function.
    def exitFunction(self, ctx:MyAlgParser.FunctionContext):
        pass


    # Enter a parse tree produced by MyAlgParser#args.
    def enterArgs(self, ctx:MyAlgParser.ArgsContext):
        pass

    # Exit a parse tree produced by MyAlgParser#args.
    def exitArgs(self, ctx:MyAlgParser.ArgsContext):
        pass


    # Enter a parse tree produced by MyAlgParser#arg.
    def enterArg(self, ctx:MyAlgParser.ArgContext):
        pass

    # Exit a parse tree produced by MyAlgParser#arg.
    def exitArg(self, ctx:MyAlgParser.ArgContext):
        pass


    # Enter a parse tree produced by MyAlgParser#assignSt.
    def enterAssignSt(self, ctx:MyAlgParser.AssignStContext):
        pass

    # Exit a parse tree produced by MyAlgParser#assignSt.
    def exitAssignSt(self, ctx:MyAlgParser.AssignStContext):
        pass


    # Enter a parse tree produced by MyAlgParser#newVar.
    def enterNewVar(self, ctx:MyAlgParser.NewVarContext):
        pass

    # Exit a parse tree produced by MyAlgParser#newVar.
    def exitNewVar(self, ctx:MyAlgParser.NewVarContext):
        pass


    # Enter a parse tree produced by MyAlgParser#label.
    def enterLabel(self, ctx:MyAlgParser.LabelContext):
        pass

    # Exit a parse tree produced by MyAlgParser#label.
    def exitLabel(self, ctx:MyAlgParser.LabelContext):
        pass


    # Enter a parse tree produced by MyAlgParser#left_expr.
    def enterLeft_expr(self, ctx:MyAlgParser.Left_exprContext):
        pass

    # Exit a parse tree produced by MyAlgParser#left_expr.
    def exitLeft_expr(self, ctx:MyAlgParser.Left_exprContext):
        pass


    # Enter a parse tree produced by MyAlgParser#expr.
    def enterExpr(self, ctx:MyAlgParser.ExprContext):
        pass

    # Exit a parse tree produced by MyAlgParser#expr.
    def exitExpr(self, ctx:MyAlgParser.ExprContext):
        pass


    # Enter a parse tree produced by MyAlgParser#ident.
    def enterIdent(self, ctx:MyAlgParser.IdentContext):
        pass

    # Exit a parse tree produced by MyAlgParser#ident.
    def exitIdent(self, ctx:MyAlgParser.IdentContext):
        pass


    # Enter a parse tree produced by MyAlgParser#pointer.
    def enterPointer(self, ctx:MyAlgParser.PointerContext):
        pass

    # Exit a parse tree produced by MyAlgParser#pointer.
    def exitPointer(self, ctx:MyAlgParser.PointerContext):
        pass


    # Enter a parse tree produced by MyAlgParser#array_access.
    def enterArray_access(self, ctx:MyAlgParser.Array_accessContext):
        pass

    # Exit a parse tree produced by MyAlgParser#array_access.
    def exitArray_access(self, ctx:MyAlgParser.Array_accessContext):
        pass



del MyAlgParser