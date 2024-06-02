# Generated from translator/asm/MyAssembler.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MyAssemblerParser import MyAssemblerParser
else:
    from MyAssemblerParser import MyAssemblerParser

# This class defines a complete listener for a parse tree produced by MyAssemblerParser.
class MyAssemblerListener(ParseTreeListener):

    # Enter a parse tree produced by MyAssemblerParser#program.
    def enterProgram(self, ctx:MyAssemblerParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#program.
    def exitProgram(self, ctx:MyAssemblerParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#line.
    def enterLine(self, ctx:MyAssemblerParser.LineContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#line.
    def exitLine(self, ctx:MyAssemblerParser.LineContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#label.
    def enterLabel(self, ctx:MyAssemblerParser.LabelContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#label.
    def exitLabel(self, ctx:MyAssemblerParser.LabelContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#name.
    def enterName(self, ctx:MyAssemblerParser.NameContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#name.
    def exitName(self, ctx:MyAssemblerParser.NameContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#instruction.
    def enterInstruction(self, ctx:MyAssemblerParser.InstructionContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#instruction.
    def exitInstruction(self, ctx:MyAssemblerParser.InstructionContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#op.
    def enterOp(self, ctx:MyAssemblerParser.OpContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#op.
    def exitOp(self, ctx:MyAssemblerParser.OpContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#op0.
    def enterOp0(self, ctx:MyAssemblerParser.Op0Context):
        pass

    # Exit a parse tree produced by MyAssemblerParser#op0.
    def exitOp0(self, ctx:MyAssemblerParser.Op0Context):
        pass


    # Enter a parse tree produced by MyAssemblerParser#op1.
    def enterOp1(self, ctx:MyAssemblerParser.Op1Context):
        pass

    # Exit a parse tree produced by MyAssemblerParser#op1.
    def exitOp1(self, ctx:MyAssemblerParser.Op1Context):
        pass


    # Enter a parse tree produced by MyAssemblerParser#op2.
    def enterOp2(self, ctx:MyAssemblerParser.Op2Context):
        pass

    # Exit a parse tree produced by MyAssemblerParser#op2.
    def exitOp2(self, ctx:MyAssemblerParser.Op2Context):
        pass


    # Enter a parse tree produced by MyAssemblerParser#op3.
    def enterOp3(self, ctx:MyAssemblerParser.Op3Context):
        pass

    # Exit a parse tree produced by MyAssemblerParser#op3.
    def exitOp3(self, ctx:MyAssemblerParser.Op3Context):
        pass


    # Enter a parse tree produced by MyAssemblerParser#operand.
    def enterOperand(self, ctx:MyAssemblerParser.OperandContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#operand.
    def exitOperand(self, ctx:MyAssemblerParser.OperandContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#final_addr.
    def enterFinal_addr(self, ctx:MyAssemblerParser.Final_addrContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#final_addr.
    def exitFinal_addr(self, ctx:MyAssemblerParser.Final_addrContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#final_addr_label.
    def enterFinal_addr_label(self, ctx:MyAssemblerParser.Final_addr_labelContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#final_addr_label.
    def exitFinal_addr_label(self, ctx:MyAssemblerParser.Final_addr_labelContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#bit_depth.
    def enterBit_depth(self, ctx:MyAssemblerParser.Bit_depthContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#bit_depth.
    def exitBit_depth(self, ctx:MyAssemblerParser.Bit_depthContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#integer.
    def enterInteger(self, ctx:MyAssemblerParser.IntegerContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#integer.
    def exitInteger(self, ctx:MyAssemblerParser.IntegerContext):
        pass


    # Enter a parse tree produced by MyAssemblerParser#string.
    def enterString(self, ctx:MyAssemblerParser.StringContext):
        pass

    # Exit a parse tree produced by MyAssemblerParser#string.
    def exitString(self, ctx:MyAssemblerParser.StringContext):
        pass



del MyAssemblerParser