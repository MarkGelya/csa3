from isa.Instructions import *
from utils.formatters import *


class Code:
    def __init__(self):
        self.mem = bytes()
        self.pointer = 0
        self.labels = {}
        self.currOp = Instruction()
        self.currOperand = None
        self.listing = list()

    def addLabel(self, name: str):
        self.labels[name] = self.pointer + self.currOp.getSize()
        # print("Label:", name, self.pointer)

    def addOperator(self, name: str):
        self.pointer += self.currOp.getSize()
        self.currOp = instructions[name]()
        self.listing.append(self.currOp)
        # print("Operand:", name, self.pointer, self.currOp.getSize())

    def addOperandInt(self, value: int):
        self.currOp.addOperand(OperandInt(value))

    def addOperandLabel(self, name: str):
        self.currOp.addOperand(OperandLabel(name))

    def addOperandFinalAddr(self, value: int):
        self.currOp.addOperand(OperandFinalAddr(value))

    def addOperandFinalLabel(self, name: str):
        self.currOp.addOperand(OperandFinalLabel(name))

    def addOperandBitDepth(self, name: str):
        self.currOp.setBitDepth(OperandBitDepth(name))

    def addOperandString(self, string: str):
        self.currOp.addOperand(OperandString(string))

    def eof(self):
        # self.pointer += self.currOp.getSize()
        # self.listing.append(self.currOp)
        pass

    def compile(self, filename):
        for el in self.listing:
            self.mem += el.compile(self.labels)
        file = open(filename, 'wb')
        file.write(self.mem)
        file.close()

    def print(self):
        for el in self.listing:
            self.mem += el.compile(self.labels)
        i = 0
        for b in self.mem:
            print(f'{hexToStr(i, 4)}: {hexToStr(b, 2)} {binToStr(b, 8)} {binCmd8(b)}')
            i += 1
