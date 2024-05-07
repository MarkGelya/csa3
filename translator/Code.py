from translator.Instructions import *

def _hex8(value: int):
    value += 0x100
    return f'0x{str(hex(value))[3:]}'

def _bin8(value: int):
    value += 0x100
    return f'0b{str(bin(value))[3:]}'

def _binCmd8(value: int):
    value += 0x100
    return f'0b{str(bin(value))[3:8]}_{str(bin(value))[8:10]}_{str(bin(value))[10:]}'


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
    def addOperandInt(self, value: int):
        self.currOp.addOperand(OperandInt(value))
    def addOperandLabel(self, name: str):
        self.currOp.addOperand(OperandLabel(name))
    def addOperandFinalAddr(self, value: int):
        self.currOp.addOperand(OperandFinalAddr(value))
    def addOperandFinalLabel(self, name: str):
        self.currOp.addOperand(OperandFinalLabel(name))
    def eof(self):
        self.pointer += self.currOp.getSize()
        self.listing.append(self.currOp)
    def print(self):
        for el in self.listing:
            self.mem += el.compile(self.labels)
        i = 0
        for b in self.mem:
            print(f'{_hex8(i)}: {_hex8(b)} {_bin8(b)} {_binCmd8(b)}')
            i += 1
