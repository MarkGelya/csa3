import logging

from transitions import State

from hardware.cpu.interface_eu import InterfaceEU
from isa.Instructions import IsaMasks
from hardware.utils.customFSM import CustomFSM

logger = logging.getLogger(__name__)


class Instruction(CustomFSM):
    def __init__(self, states, eu: InterfaceEU, op_code: int):
        super().__init__(states)
        self.op_code = op_code
        self.eu = eu

    def __str__(self):
        return type(self).__name__

    def finishInstr(self):
        self.eu.wire_instr.set_high()
        self.eu.set_state(InterfaceEU.stateInstrFetch)

class SimpleInstruction(Instruction):
    stateExec0 = State('Exec0')
    stateExec1 = State('Exec1')
    states = [stateExec0, stateExec1]
    def __init__(self, eu: InterfaceEU, op_code: int):
        super().__init__(self.states, eu, op_code)

class InstructionAddr(Instruction):
    stateStart = State('Start')
    stateLoadOperand0 = State('LoadOperand0')
    stateLoadOperand1 = State('LoadOperand1')
    stateAddrFetch0 = State('AddrFetch0')
    stateAddrFetch1 = State('AddrFetch1')
    stateExec0 = State('Exec0')
    stateExec1 = State('Exec1')
    states = [
        stateStart,
        stateExec0, stateExec1,
        stateLoadOperand0, stateLoadOperand1,
        stateAddrFetch0, stateAddrFetch1,
    ]
    def __init__(self, eu: InterfaceEU, op_code: int):
        super().__init__(InstructionAddr.states, eu, op_code)
        self.byte_depth = (op_code & IsaMasks.bit_depth) >> 1
        self.byte_depth_counter = 0

    def skipAddr(self):
        self.eu.wire_skip_addr.set_high()

    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            self.eu.wire_operand.set_high()
            if self.op_code & IsaMasks.final_addr:
                self.eu.wire_indirect_addr.set_high()
                self.set_state(InstructionAddr.stateAddrFetch0)
            else:
                self.eu.wire_direct_addr.set_high()
                self.set_state(InstructionAddr.stateLoadOperand0)
                self.eu.alu.set_b(0)
        return False

    # Если в InstructionQueue находится адрес, то передать BIU команду о выборке операнда
    def phaseLoadOperand0(self):
        if self.eu.wire_operand_fetched.is_high():
            if self.byte_depth_counter <= self.byte_depth:
                self.eu.alu.set_b(self.eu.alu.get_b() | (
                        self.eu.bus_data1.get_value() << (8 * (self.byte_depth - self.byte_depth_counter)))
                )
                self.byte_depth_counter += 1
                self.set_state(InstructionAddr.stateLoadOperand0)
        if self.byte_depth_counter > self.byte_depth:
            self.eu.wire_skip_addr.set_high()
            self.set_state(InstructionAddr.stateExec0)
        if self.byte_depth_counter <= self.byte_depth:
            self.eu.wire_operand.set_high()
            self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
            self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
            if self.op_code & IsaMasks.final_addr:
                self.eu.wire_indirect_addr.set_high()
            else:
                self.eu.wire_direct_addr.set_high()
        return False

    def phaseLoadOperand1(self):
        # if self.byte_depth_counter <= self.byte_depth:
        #     self.eu.wire_operand.set_high()
        #     self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
        #     self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
        #     if self.op_code & IsaMasks.final_addr:
        #         self.eu.wire_indirect_addr.set_high()
        #     else:
        #         self.eu.wire_direct_addr.set_high()
        # if self.eu.wire_operand_fetched.is_high():
        #     if self.byte_depth_counter <= self.byte_depth:
        #         self.eu.alu.set_b(self.eu.alu.get_b() | (self.eu.bus_data.get_value() << (8 * (self.byte_depth - self.byte_depth_counter))))
        #         self.byte_depth_counter += 1
        #         self.set_state(InstructionAddr.stateLoadOperand0)
        #     else:
        #         self.eu.wire_skip_addr.set_high()
        #         self.set_state(InstructionAddr.stateExec0)
        return False

    # Если в InstructionQueue находится адрес, то передать BIU команду о выборке конечного адреса
    def phaseAddrFetch0(self):
        self.eu.wire_indirect_addr.set_high()
        if self.eu.wire_addr_ready.is_high():
            return True
        return False

    def phaseAddrFetch1(self):
        self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
        self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
        self.eu.wire_indirect_addr.set_high()
        if self.eu.wire_biu_is_wait.is_high():
            self.eu.wire_operand.set_high()
            self.set_state(InstructionAddr.stateLoadOperand0)
        return False

class InstructionJump(Instruction):
    stateStart = State('Start')
    stateExec0 = State('Exec0')
    stateExec1 = State('Exec1')
    states = [
        stateStart,
        stateExec0, stateExec1,
    ]

    def __init__(self, eu: InterfaceEU, op_code: int):
        super().__init__(InstructionAddr.states, eu, op_code)
        self.byte_depth = (op_code & IsaMasks.bit_depth) >> 1
        self.byte_depth_counter = 0
        self.is_jumped = False

    def skipAddr(self):
        self.eu.wire_skip_addr.set_high()

    def phaseExec0(self):
        if self.is_jumped:
            self.eu.wire_drop.set_high()
            return True
        else:
            self.skipAddr()
            return True

    def phaseExec1(self):
        self.finishInstr()
        return False


class InstructionPort(Instruction):
    pass

class HLT(SimpleInstruction):
    def __init__(self, eu: InterfaceEU, op_code: int):
        super().__init__(eu, op_code)

    def phaseExec0(self):
        if self.eu.wire_run.is_high():
            self.finishInstr()
        else:
            self.eu.set_state(InterfaceEU.stateHlt)
        return False

class NOP(SimpleInstruction):
    pass

class LD(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.set_a(self.eu.alu.get_b())
        self.finishInstr()
        return False

    def phaseExec1(self):
        return False

class ST(InstructionAddr):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if self.op_code & IsaMasks.final_addr:
                self.set_state(InstructionAddr.stateAddrFetch0)
            else:
                self.set_state(InstructionAddr.stateLoadOperand0)
        return False

    # Если в InstructionQueue находится адрес, то передать BIU команду о выборке операнда
    def phaseLoadOperand0(self):
        self.eu.wire_operand.set_high()
        self.eu.wire_read.set_low()
        self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
        self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
        if self.op_code & IsaMasks.final_addr:
            self.eu.wire_indirect_addr.set_high()
        else:
            self.eu.wire_direct_addr.set_high()
        self.eu.bus_data2.set_value(
            (self.eu.alu.get_a() >> (8 * (self.byte_depth - self.byte_depth_counter))) & 0xFF
        )
        return True

    def phaseLoadOperand1(self):
        if self.eu.wire_operand_fetched.is_high():
            if self.byte_depth_counter < self.byte_depth:
                self.byte_depth_counter += 1
            else:
                self.eu.wire_skip_addr.set_high()
                self.set_state(InstructionAddr.stateExec0)
                return False
        self.eu.wire_operand.set_high()
        self.eu.wire_read.set_low()
        self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
        self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
        if self.op_code & IsaMasks.final_addr:
            self.eu.wire_indirect_addr.set_high()
        else:
            self.eu.wire_direct_addr.set_high()
        self.eu.bus_data2.set_value(
            (self.eu.alu.get_a() >> (8 * (self.byte_depth - self.byte_depth_counter))) & 0xFF
        )
        return False

    def phaseAddrFetch0(self):
        self.eu.wire_indirect_addr.set_high()
        self.eu.wire_read.set_low()
        if self.eu.wire_addr_ready.is_high():
            return True
        return False

    def phaseAddrFetch1(self):
        self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
        self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
        self.eu.wire_indirect_addr.set_high()
        self.eu.wire_read.set_low()
        if self.eu.wire_biu_is_wait.is_high():
            self.eu.wire_operand.set_high()
            self.set_state(InstructionAddr.stateLoadOperand0)
        return False

    def phaseExec0(self):
        self.finishInstr()
        return False

    def phaseExec1(self):
        return False

class ADD(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.ADD()
        self.finishInstr()
        return False

class SUB(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.SUB()
        self.finishInstr()
        return False

class INC(SimpleInstruction):
    def phaseExec0(self):
        self.eu.alu.INC()
        self.finishInstr()
        return False
    pass

class DEC(SimpleInstruction):
    def phaseExec0(self):
        self.eu.alu.DEC()
        self.finishInstr()
        return False
    pass

class NOT(SimpleInstruction):
    def phaseExec0(self):
        self.eu.alu.NOT()
        self.finishInstr()
        return False
    pass

class OR(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.OR()
        self.finishInstr()
        return False
    pass

class AND(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.AND()
        self.finishInstr()
        return False
    pass

class XOR(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.XOR()
        self.finishInstr()
        return False
    pass

class CMP(InstructionAddr):
    def phaseExec0(self):
        self.eu.alu.CMP()
        self.finishInstr()
        return False

class JMP(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            self.eu.wire_jump.set_high()
            self.is_jumped = True
            return True
        return False

class JZ(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if self.eu.alu.flags_ZF:
                self.eu.wire_jump.set_high()
                self.is_jumped = True
            return True
        return False

class JNZ(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if not self.eu.alu.flags_ZF:
                self.eu.wire_jump.set_high()
                self.is_jumped = True
            return True
        return False

class JG(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if self.eu.alu.flags_ZF and (self.eu.alu.flags_NF == self.eu.alu.flags_OF):
                self.eu.wire_jump.set_high()
                self.is_jumped = True
            return True
        return False

class JGE(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if self.eu.alu.flags_NF == self.eu.alu.flags_OF:
                self.eu.wire_jump.set_high()
                self.is_jumped = True
            return True
        return False

class JL(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if self.eu.alu.flags_NF != self.eu.alu.flags_OF:
                self.eu.wire_jump.set_high()
                self.is_jumped = True
            return True
        return False

class JLE(InstructionJump):
    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            if self.eu.alu.flags_ZF or (self.eu.alu.NF != self.eu.alu.flags_OF):
                self.eu.wire_jump.set_high()
                self.is_jumped = True
            return True
        return False

class IN(InstructionPort):
    stateStart = State('Start')
    stateExec0 = State('Exec0')
    stateExec1 = State('Exec1')
    states = [
        stateStart,
        stateExec0, stateExec1,
    ]

    def __init__(self, eu: InterfaceEU, op_code: int):
        super().__init__(InstructionAddr.states, eu, op_code)
        self.byte_depth = (op_code & IsaMasks.bit_depth) >> 1
        self.byte_depth_counter = 0

    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            self.eu.wire_operand.set_high()
            self.eu.wire_direct_addr.set_high()
            self.eu.wire_mem.set_low()
            self.eu.alu.set_b(0)
            self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
            self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
            if self.eu.wire_biu_is_wait.is_high():
                return True
        return False

    def phaseExec0(self):
        if self.eu.wire_operand_fetched.is_high():
            if self.byte_depth_counter <= self.byte_depth:
                self.eu.alu.set_b(self.eu.alu.get_b() | (
                    self.eu.bus_data1.get_value() << (8 * (self.byte_depth - self.byte_depth_counter)))
                )
                self.byte_depth_counter += 1
        if self.byte_depth_counter > self.byte_depth:
            self.eu.wire_skip_addr.set_high()
            return True
        else:
            if self.eu.wire_biu_is_wait.is_high():
                self.eu.wire_direct_addr.set_high()
                self.eu.wire_mem.set_low()
                self.eu.wire_operand.set_high()
                self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
                self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
            return False

    def phaseExec1(self):
        self.eu.alu.set_a(self.eu.alu.get_b())
        self.finishInstr()
        return False

class OUT(InstructionPort):
    stateStart = State('Start')
    stateExec0 = State('Exec0')
    stateExec1 = State('Exec1')
    states = [
        stateStart,
        stateExec0, stateExec1,
    ]

    def __init__(self, eu: InterfaceEU, op_code: int):
        super().__init__(InstructionAddr.states, eu, op_code)
        self.byte_depth = (op_code & IsaMasks.bit_depth) >> 1
        self.byte_depth_counter = 0

    def phaseStart(self):
        if self.eu.wire_addr_ready.is_high():
            self.eu.wire_operand.set_high()
            self.eu.wire_direct_addr.set_high()
            self.eu.wire_mem.set_low()
            self.eu.wire_read.set_low()
            self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
            self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
            self.eu.bus_data2.set_value(
                (self.eu.alu.get_a() >> (8 * (self.byte_depth - self.byte_depth_counter))) & 0xFF
            )
            if self.eu.wire_biu_is_wait.is_high():
                return True
        return False

    def phaseExec0(self):
        if self.eu.wire_operand_fetched.is_high():
            if self.byte_depth_counter < self.byte_depth:
                self.byte_depth_counter += 1
            else:
                self.eu.wire_skip_addr.set_high()
                return True
        self.eu.wire_bit_depth0.set_level(self.byte_depth_counter & 0b01)
        self.eu.wire_bit_depth1.set_level(self.byte_depth_counter & 0b10)
        self.eu.bus_data2.set_value(
            (self.eu.alu.get_a() >> (8 * (self.byte_depth - self.byte_depth_counter))) & 0xFF
        )
        return False

    def phaseExec1(self):
        self.finishInstr()
        return False

isa = {
    0b000_01111:   HLT,
    0b000_00000:   NOP,

    0b000_10001:   INC,
    0b000_10010:   DEC,

    0b000_10011:   NOT,

    0b001_00_00_0: OR,
    0b001_01_00_0: AND,
    0b001_10_00_0: XOR,

    0b010_00_00_0: LD,
    0b010_01_00_0: ST,

    0b011_00_00_0: ADD,
    0b011_01_00_0: SUB,
    0b011_10_00_0: CMP,

    0b100_0000_0:  JMP,
    0b100_0001_0:  JZ,
    0b100_0010_0:  JNZ,
    0b100_0011_0:  JG,
    0b100_0100_0:  JGE,
    0b100_0101_0:  JL,
    0b100_0110_0:  JLE,

    0b101_00000:   IN,
    0b110_00000:   OUT,
}

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
