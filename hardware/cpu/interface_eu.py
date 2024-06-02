from transitions import State

from hardware.base.register import Register
from hardware.cpu.alu import ALU32
from hardware.base.bus import Bus
from hardware.base.wire import Wire
from hardware.utils.customFSM import CustomFSM


class InterfaceEU(CustomFSM):
    stateWait = State('Wait')
    stateInstrFetch = State('InstructionFetch')
    stateExecution = State('Execution')
    stateHlt = State('Hlt')
    states = [stateWait, stateInstrFetch, stateExecution, stateHlt]

    def __init__(self):
        super().__init__(self.states)

        self._CR = Register(8)
        self.cmd = None
        self.alu = ALU32()

        # Flags
        self.flag_eof = False

        # Input buses
        self.bus_instr = Bus(8)
        self.bus_data1 = Bus(8)

        # Output buses
        self.bus_data2 = Bus(8)

        # Output wires
        self.wire_direct_addr = Wire(default=Wire.low_level)
        self.wire_indirect_addr = Wire(default=Wire.low_level)
        self.wire_operand = Wire(default=Wire.low_level)
        self.wire_mem = Wire(default=Wire.high_level)
        self.wire_read = Wire(default=Wire.high_level)
        self.wire_bit_depth0 = Wire(default=Wire.low_level)
        self.wire_bit_depth1 = Wire(default=Wire.low_level)
        self.wire_operand = Wire(default=Wire.low_level)
        self.wire_jump = Wire(default=Wire.low_level)
        self.wire_drop = Wire(default=Wire.low_level)
        self.wire_skip = Wire(default=Wire.low_level)
        self.wire_skip_addr = Wire(default=Wire.low_level)
        self.wire_hlt = Wire(default=Wire.low_level)

        # Test output wires
        self.wire_instr = Wire(default=Wire.low_level)

        # Input wires
        self.wire_instr_ready = Wire()
        self.wire_addr_ready = Wire()
        self.wire_operand_fetched = Wire()
        self.wire_biu_is_wait = Wire()
        self.wire_run = Wire(default=Wire.low_level)

    def phaseWait(self):
        pass

    def phaseInstructionFetch(self):
        pass

    def phaseExecution(self):
        pass

    def __str__(self):
        pass