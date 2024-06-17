from isa.Instructions import *
from utils.formatters import *


class Code:
    def __init__(self):
        self.mem = b""
        self.pointer = 0
        self.labels = {}
        self.currOp = Instruction()
        self.currOperand = None
        self.listing = list()

    def add_label(self, name: str):
        self.labels[name] = self.pointer + self.currOp.getSize()
        # print("Label:", name, self.pointer)

    def add_operator(self, name: str):
        self.pointer += self.currOp.getSize()
        self.currOp = instructions[name]()
        self.listing.append(self.currOp)
        # print("Operand:", name, self.pointer, self.currOp.getSize())

    def add_operand_int(self, value: int):
        self.currOp.addOperand(OperandInt(value))

    def add_operand_label(self, name: str):
        self.currOp.addOperand(OperandLabel(name))

    def add_operand_final_addr(self, value: int):
        self.currOp.addOperand(OperandFinalAddr(value))

    def add_operand_final_label(self, name: str):
        self.currOp.addOperand(OperandFinalLabel(name))

    def add_operand_bit_depth(self, name: str):
        self.currOp.setBitDepth(OperandBitDepth(name))

    def add_operand_string(self, string: str):
        self.currOp.addOperand(OperandString(string))

    def eof(self):
        # self.pointer += self.currOp.getSize()
        # self.listing.append(self.currOp)
        pass

    def compile(self, filename):
        for el in self.listing:
            self.mem += el.compile(self.labels)
        file = open(filename, "wb")
        file.write(self.mem)
        file.close()

    def print(self):
        for el in self.listing:
            self.mem += el.compile(self.labels)
        i = 0
        for b in self.mem:
            print(f"{hex_to_str(i, 4)}: {hex_to_str(b, 2)} {bin_to_str(b, 8)} {binCmd8(b)}")
            i += 1
