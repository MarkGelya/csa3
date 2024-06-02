from dataclasses import dataclass
from isa.Instructions import isa as __isa
from isa.Instructions import IsaMasks
# withou args
# with args
#   addr
#   *addr
#   port

isa = dict((v, k) for k, v in __isa.items())

def instrByOpCode(op_code: int):
    type = op_code & IsaMasks.type
    if type == 0b000_00000:
        pass
    elif (type == 0b001_00000) or (type == 0b010_00000) or (type == 0b011_00000):
        op_code &= (IsaMasks.final_addr ^ IsaMasks.byte)
        op_code &= (IsaMasks.bit_depth ^ IsaMasks.byte)
    elif type == 0b100_00000:
        op_code &= (IsaMasks.final_addr ^ IsaMasks.byte)
    elif (type == 0b101_00000) or (type == 0b110_00000):
        op_code &= (IsaMasks.port ^ IsaMasks.byte)
    return isa[op_code]

class Instruction:
    def __init__(self, op_code):
        self.op_code = op_code
    def exec(self):
        pass
    def __str__(self):
        return type(self).__name__
class SimpleInstruction(Instruction):
    pass

class InstructionAddr(Instruction):
    pass

class InstructionPort(ExecutableInstruction):
    pass

class HLT(SimpleInstruction):
    pass

class NOP(SimpleInstruction):
    pass

class LD(InstructionAddr):
    pass

class ST(InstructionAddr):
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

class IN(InstructionPort):
    pass

class OUT(InstructionPort):
    pass