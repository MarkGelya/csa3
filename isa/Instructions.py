from dataclasses import dataclass


class CompileError(Exception):
    pass


class InvalidOperatorError(CompileError):
    pass


class OperandCountError(CompileError):
    pass


# withou args
# with args
#   addr
#   *addr
#   port
#

isa = {
    "HLT": 0b000_01111,
    "NOP": 0b000_00000,
    "INC": 0b000_10001,
    "DEC": 0b000_10010,
    "NOT": 0b000_10011,
    "OR": 0b001_00_11_0,
    "AND": 0b001_01_11_0,
    "XOR": 0b001_10_11_0,
    "LD": 0b010_00_11_0,
    "ST": 0b010_01_11_0,
    "ADD": 0b011_00_11_0,
    "SUB": 0b011_01_11_0,
    "CMP": 0b011_10_11_0,
    "JMP": 0b100_0000_0,
    "JZ": 0b100_0001_0,
    "JNZ": 0b100_0010_0,
    "JG": 0b100_0011_0,
    "JGE": 0b100_0100_0,
    "JL": 0b100_0101_0,
    "JLE": 0b100_0110_0,
    "JEOF": 0b100_0111_0,
    "IN": 0b101_00000,
    "OUT": 0b110_00000,
}

_isa2 = dict((v, k) for k, v in isa.items())


@dataclass
class IsaMasks:
    byte = 0b1111_1111
    type = 0b1110_0000
    final_addr = 0b0000_0001
    port = 0b0001_1111
    bit_depth = 0b0000_0110
    bit_depth0 = 0b0000_0010
    bit_depth1 = 0b0000_0100


def instrBy(op_code: int):
    type_cmd = op_code & IsaMasks.type
    if type_cmd == 0b000_00000:
        pass
    elif (type_cmd == 0b001_00000) or (type_cmd == 0b010_00000) or (type_cmd == 0b011_00000):
        op_code &= IsaMasks.final_addr ^ IsaMasks.byte
        op_code &= IsaMasks.bit_depth ^ IsaMasks.byte
    elif type_cmd == 0b100_00000:
        op_code &= IsaMasks.final_addr ^ IsaMasks.byte
    elif (type_cmd == 0b101_00000) or (type_cmd == 0b110_00000):
        op_code &= IsaMasks.port ^ IsaMasks.byte
    return _isa2[op_code]


class Operand:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{type(self).__name__}: {self.value}"


class OperandInt(Operand):
    def __str__(self):
        return f"{type(self).__name__}: {hex(self.value)}"


class OperandFinalAddr(Operand):
    def __str__(self):
        return f"{type(self).__name__}: {hex(self.value)}"


class OperandLabel(Operand):
    pass


class OperandFinalLabel(Operand):
    pass


class OperandBitDepth(Operand):
    def updateCmd(self, cmd):
        if self.value == "b8":
            cmd ^= IsaMasks.bit_depth0
            cmd ^= IsaMasks.bit_depth1
        elif self.value == "b16":
            cmd ^= IsaMasks.bit_depth1
        elif self.value == "b24":
            cmd ^= IsaMasks.bit_depth1
        elif self.value == "b32":
            pass
        else:
            pass
        return cmd


class OperandString(Operand):
    pass


class Instruction:
    def __init__(self):
        self.max_operators = 0
        self.operands = list()

    def getSize(self):
        return 0

    def getBytes(self):
        pass

    def setBitDepth(self, value):
        pass

    def addOperand(self, operand):
        if len(self.operands) == self.max_operators:
            raise OperandCountError(f"Expected {self.max_operators} operands")
        self.operands.append(operand)

    def compile(self, labels):
        return isa[type(self).__name__].to_bytes(1)

    def __str__(self):
        return type(self).__name__


class ImaginaryInstruction(Instruction):
    pass


class ExecutableInstruction(Instruction):
    pass


class SimpleInstruction(ExecutableInstruction):
    def getSize(self):
        return 1

    pass


class InstructionAddr(ExecutableInstruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 2
        self.operand = None
        self.bit_depth = OperandBitDepth("b32")

    def setBitDepth(self, operand):
        self.bit_depth = operand
        self.operands.append(operand)

    def addOperand(self, operand):
        if len(self.operands) == self.max_operators:
            raise OperandCountError(f"Expected {self.max_operators} operands")
        self.operands.append(operand)

    def getSize(self):
        return 3

    def getBytes(self):
        pass

    def compile(self, labels):
        cmd = isa[type(self).__name__]
        cmd = self.bit_depth.updateCmd(cmd)
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
        elif type(operand) == OperandFinalAddr:
            value = operand.value
            cmd = cmd | IsaMasks.final_addr
        elif type(operand) == OperandLabel:
            value = labels[operand.value]
        elif type(operand) == OperandFinalLabel:
            value = labels[operand.value]
            cmd = cmd | IsaMasks.final_addr
        return cmd.to_bytes(1) + value.to_bytes(2, "big")

    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'


class InstructionPort(ExecutableInstruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 1
        self.operand = None
        self.bit_depth = OperandBitDepth("b32")

    def setBitDepth(self, operand):
        self.bit_depth = operand
        self.operands.append(operand)

    def addOperand(self, operand):
        if len(self.operands) == self.max_operators:
            raise OperandCountError(f"Expected {self.max_operators} operands")
        self.operands.append(operand)

    def getSize(self):
        return 3

    def getBytes(self):
        pass

    def compile(self, labels):
        cmd = isa[type(self).__name__]
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
        return cmd.to_bytes(1) + value.to_bytes(2, "big")

    # def addOperand(self, operand):
    #     if len(self.operands) == self.max_operators:
    #         raise OperandCountException(f'Expected {self.max_operators} operands')
    #     self.operands.append(operand)
    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'


class WORD(ImaginaryInstruction):
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
        elif type(operand) == OperandLabel:
            value = labels[operand.value]
        elif type(operand) == OperandFinalLabel:
            value = labels[operand.value]
        return value.to_bytes(self.getSize(), "big")

    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'


class SHORT(WORD):
    def getSize(self):
        return 2


class BYTE(ImaginaryInstruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 1

    def getSize(self):
        return 1

    def compile(self, labels):
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
        return value.to_bytes(self.getSize(), "big")

    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'


class BYTES(ImaginaryInstruction):
    def __init__(self):
        super().__init__()
        self.max_operators = 1

    def getSize(self):
        if len(self.operands) > 0:
            operand = self.operands[0]
            if type(operand) == OperandInt:
                return operand.value
            elif type(operand) == OperandString:
                value = operand.value[1:-1]
                return len(
                    (bytearray([len(value)]) if len(value) < 256 else bytearray([0xFF])) + value.encode("ASCII")[:256]
                )
        else:
            return 0

    def compile(self, labels):
        operand = self.operands[0]
        value = 0
        if type(operand) == OperandInt:
            value = operand.value
            return value.to_bytes(self.getSize(), "big")
        elif type(operand) == OperandString:
            value = operand.value[1:-1]
            return (bytearray([len(value)]) if len(value) < 256 else bytearray([0xFF])) + value.encode("ASCII")[:256]

    def __str__(self):
        return f'{type(self).__name__} [{",".join(str(el) for el in self.operands)}]'


class HLT(SimpleInstruction):
    pass


class NOP(SimpleInstruction):
    pass


class LD(InstructionAddr):
    pass


class LD8(InstructionAddr):
    pass


class LD16(InstructionAddr):
    pass


class ST(InstructionAddr):
    pass


class ST8(InstructionAddr):
    pass


class ST16(InstructionAddr):
    pass


class ADD(InstructionAddr):
    pass


class SUB(InstructionAddr):
    pass


class INC(SimpleInstruction):
    pass


class DEC(SimpleInstruction):
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


class JEOF(InstructionAddr):
    pass


class IN(InstructionPort):
    pass


class OUT(InstructionPort):
    pass


instructions = {
    "WORD": WORD,
    "SHORT": SHORT,
    "BYTE": BYTE,
    "BYTES": BYTES,
    "HLT": HLT,
    "NOP": NOP,
    "LD": LD,
    "ST": ST,
    "ADD": ADD,
    "SUB": SUB,
    "INC": INC,
    "DEC": DEC,
    "OR": OR,
    "AND": AND,
    "XOR": XOR,
    "NOT": NOT,
    "CMP": CMP,
    "JMP": JMP,
    "JZ": JZ,
    "JNZ": JNZ,
    "JG": JG,
    "JGE": JGE,
    "JL": JL,
    "JLE": JLE,
    "JEOF": JEOF,
    "IN": IN,
    "OUT": OUT,
}
