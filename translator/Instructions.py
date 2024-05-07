class CompileException(Exception):
    pass

class InvalidOperatorException(CompileException):
    pass

class OperandCountException(CompileException):
    pass

_instructions = {
    'HLT':  0b00000_00_0,
    'NOP':  0b00001_00_0,

    'LD':   0b00100_00_0,
    'ST':   0b00101_00_0,

    'ADD':  0b01000_00_0,
    'SUB':  0b01001_00_0,

    'INC':  0b01010_00_0,
    'DEC':  0b01011_00_0,

    'OR':   0b01100_00_0,
    'AND':  0b01101_00_0,
    'XOR':  0b01110_00_0,
    'NOT':  0b01111_00_0,

    'CMP':  0b10000_00_0,

    'JMP':  0b10001_00_0,
    'JZ':   0b10010_00_0,
    'JNZ':  0b10011_00_0,
    'JG':   0b10100_00_0,
    'JGE':  0b10101_00_0,
    'JL':   0b10110_00_0,
    'JLE':  0b10111_00_0,

    'IN':   0b11000_00_0,
    'OUT':  0b11001_00_0,
}

final_flag = 0b00000_00_1

class Operand:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'{type(self).__name__}: {self.value}'

class OperandInt(Operand):
    def __str__(self):
        return f'{type(self).__name__}: {hex(self.value)}'

class OperandFinalAddr(Operand):
    def __str__(self):
        return f'{type(self).__name__}: {hex(self.value)}'

class OperandLabel(Operand):
    pass

class OperandFinalLabel(Operand):
    pass


class Instruction:
    def __init__(self):
        self.max_operators = 0
        self.operands = list()
    def getSize(self):
        return 0
    def getBytes(self):
        pass
    def addOperand(self, operand):
        if len(self.operands) == self.max_operators:
            raise OperandCountException(f'Expected {self.max_operators} operands')
        self.operands.append(operand)
    def compile(self, labels):
        return _instructions[type(self).__name__].to_bytes(1, 'little')
    def __str__(self):
        return type(self).__name__

class InstructionAddr(Instruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 1
    def getSize(self):
        return 3
    def getBytes(self):
        pass
    # def addOperand(self, operand):
    #     if len(self.operands) == self.max_operators:
    #         raise OperandCountException(f'Expected {self.max_operators} operands')
    #     self.operands.append(operand)
    def compile(self, labels):
        cmd = _instructions[type(self).__name__]
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
        elif type(operand) == OperandFinalAddr:
            value = operand.value
            cmd = cmd | final_flag
        elif type(operand) == OperandLabel:
            value = labels[operand.value]
        elif type(operand) == OperandFinalLabel:
            value = labels[operand.value]
            cmd = cmd | final_flag
        return cmd.to_bytes(1, 'little') + value.to_bytes(2, 'little')
    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'

class InstructionPort(Instruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 1
    def getSize(self):
        return 2
    def getBytes(self):
        pass
    def compile(self, labels):
        cmd = _instructions[type(self).__name__]
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
        return cmd.to_bytes(1, 'little') + value.to_bytes(1, 'little')
    # def addOperand(self, operand):
    #     if len(self.operands) == self.max_operators:
    #         raise OperandCountException(f'Expected {self.max_operators} operands')
    #     self.operands.append(operand)
    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'

class WORD(Instruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 1
    def getSize(self):
        return 4
    def compile(self, labels):
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
        elif type(operand) == OperandFinalAddr:
            value = operand.value
            cmd = cmd | final_flag
        elif type(operand) == OperandLabel:
            value = labels[operand.value]
        elif type(operand) == OperandFinalLabel:
            value = labels[operand.value]
            cmd = cmd | final_flag
        return value.to_bytes(4, 'little')
    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'
class HLT(Instruction):
    pass

class NOP(Instruction):
    pass

class LD(InstructionAddr):
    pass

class ST(InstructionAddr):
    pass

class ADD(InstructionAddr):
    pass

class SUB(InstructionAddr):
    pass

class INC(Instruction):
    pass

class DEC(Instruction):
    pass

class OR(InstructionAddr):
    pass

class AND(InstructionAddr):
    pass

class XOR(InstructionAddr):
    pass

class NOT(InstructionAddr):
    pass

class CMP(InstructionAddr):
    pass

class JMP(InstructionAddr):
    pass

class JZ(InstructionAddr):
    pass

class JNZ(InstructionAddr):
    pass

class JG(InstructionAddr):
    pass

class JGE(InstructionAddr):
    pass

class JL(InstructionAddr):
    pass

class JLE(InstructionAddr):
    pass

class IN(InstructionPort):
    pass

class OUT(InstructionPort):
    pass

instructions = {
    'WORD': WORD,
    # 'SHORT': SHORT,
    # 'CHAR': CHAR,
    'HLT':  HLT,
    'NOP':  NOP,
    'LD':   LD,
    'ST':   ST,
    'ADD':  ADD,
    'SUB':  SUB,
    'INC':  INC,
    'DEC':  DEC,
    'OR':   OR,
    'AND':  AND,
    'XOR':  XOR,
    'NOT':  NOT,
    'CMP':  CMP,
    'JMP':  JMP,
    'JZ':   JZ,
    'JNZ':  JNZ,
    'JG':   JG,
    'JGE':  JGE,
    'JL':   JL,
    'JLE':  JLE,
    'IN':   IN,
    'OUT':  OUT,
}
