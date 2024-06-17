# Generated from translator/asm/MyAssembler.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .MyAssemblerParser import MyAssemblerParser
else:
    from MyAssemblerParser import MyAssemblerParser

# This class defines a complete generic visitor for a parse tree produced by MyAssemblerParser.


class MyAssemblerVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by MyAssemblerParser#program.
    def visitProgram(self, ctx: MyAssemblerParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#line.
    def visitLine(self, ctx: MyAssemblerParser.LineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#label.
    def visitLabel(self, ctx: MyAssemblerParser.LabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#name.
    def visitName(self, ctx: MyAssemblerParser.NameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#instruction.
    def visitInstruction(self, ctx: MyAssemblerParser.InstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#op.
    def visitOp(self, ctx: MyAssemblerParser.OpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#op0.
    def visitOp0(self, ctx: MyAssemblerParser.Op0Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#op1.
    def visitOp1(self, ctx: MyAssemblerParser.Op1Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#op2.
    def visitOp2(self, ctx: MyAssemblerParser.Op2Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#op3.
    def visitOp3(self, ctx: MyAssemblerParser.Op3Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#operand.
    def visitOperand(self, ctx: MyAssemblerParser.OperandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#final_addr.
    def visitFinal_addr(self, ctx: MyAssemblerParser.Final_addrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#final_addr_label.
    def visitFinal_addr_label(self, ctx: MyAssemblerParser.Final_addr_labelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#bit_depth.
    def visitBit_depth(self, ctx: MyAssemblerParser.Bit_depthContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#integer.
    def visitInteger(self, ctx: MyAssemblerParser.IntegerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MyAssemblerParser#string.
    def visitString(self, ctx: MyAssemblerParser.StringContext):
        return self.visitChildren(ctx)


del MyAssemblerParser
