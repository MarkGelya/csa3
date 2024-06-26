from translator.asm.antlr4.MyAssemblerParser import MyAssemblerParser
from translator.asm.antlr4.MyAssemblerVisitor import MyAssemblerVisitor


class VisitorInterp(MyAssemblerVisitor):
    def __init__(self, code):
        self.code = code

    def visitProgram(self, ctx: MyAssemblerParser.ProgramContext):
        for line in ctx.line():
            self.visit(line)

    def visitLine(self, ctx: MyAssemblerParser.LineContext):
        if ctx.label() is not None:
            # print("Label:", ctx.label().name().getText())
            self.code.add_label(ctx.label().name().getText())
        if ctx.instruction() is not None:
            self.visit(ctx.instruction())

    def visitInstruction(self, ctx: MyAssemblerParser.InstructionContext):
        # print("Operator:", ctx.op().getText())
        self.code.add_operator(ctx.op().getText())
        for operand in ctx.operand():
            self.visit(operand)

    def visitOperand(self, ctx: MyAssemblerParser.OperandContext):
        if ctx.integer() is not None:
            # print("Operand (int):", self.visit(ctx.integer()))
            self.code.add_operand_int(self.visit(ctx.integer()))
        elif ctx.name() is not None:
            # print("Operand (label):", ctx.name().getText())
            self.code.add_operand_label(ctx.name().getText())
        elif ctx.final_addr() is not None:
            # self.visit(ctx.final_addr())
            self.code.add_operand_final_addr(self.visit(ctx.final_addr()))
        elif ctx.final_addr_label() is not None:
            # self.visit(ctx.final_addr_label())
            self.code.add_operand_final_label(self.visit(ctx.final_addr_label()))
        elif ctx.bit_depth() is not None:
            self.code.add_operand_bit_depth(self.visit(ctx.bit_depth()))
        elif ctx.string() is not None:
            self.code.add_operand_string(self.visit(ctx.string()))

    def visitFinal_addr(self, ctx: MyAssemblerParser.Final_addrContext):
        if ctx.integer() is not None:
            # print("Operand (final address):", ctx.integer().getText())
            return self.visit(ctx.integer())

    def visitFinal_addr_label(self, ctx: MyAssemblerParser.Final_addr_labelContext):
        if ctx.name() is not None:
            # print("Operand (final address label):", ctx.name().getText())
            return ctx.name().getText()

    def visitBit_depth(self, ctx: MyAssemblerParser.Bit_depthContext):
        return ctx.getText()

    def visitString(self, ctx: MyAssemblerParser.StringContext):
        return ctx.getText()

    def visitInteger(self, ctx: MyAssemblerParser.IntegerContext):
        if ctx.DEC_INTEGER() is not None:
            # print("Operand (decimal_integer):", ctx.DEC_INTEGER().getText())
            return int(ctx.DEC_INTEGER().getText())
        elif ctx.HEX_INTEGER() is not None:
            # print("Operand (hex_integer):", ctx.HEX_INTEGER().getText())
            return int(ctx.HEX_INTEGER().getText(), 16)
        elif ctx.OCT_INTEGER() is not None:
            # print("Operand (oct_integer):", ctx.OCT_INTEGER().getText())
            return int(ctx.OCT_INTEGER().getText(), 8)
        elif ctx.BIN_INTEGER() is not None:
            # print("Operand (bin_integer):", ctx.BIN_INTEGER().getText())
            return int(ctx.BIN_INTEGER().getText(), 2)
