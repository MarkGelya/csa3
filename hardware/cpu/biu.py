import logging

from transitions import State

from hardware.base.bus import Bus
from hardware.base.register import Register
from hardware.base.wire import Wire
from hardware.memory.memory import Memory
from hardware.utils.customFSM import CustomFSM

logger = logging.getLogger(__name__)
class BIU(CustomFSM):
    stateWait = State('Wait')
    stateByteFetch = State('ByteFetch')
    stateAddrFetch = State('AddrFetch')
    states = [
        stateWait,
        stateByteFetch,
        stateAddrFetch,
    ]

    # , wire_direct_addr: Wire, wire_indirect_addr: Wire, wire_addr_ready: Wire, wire_writable: Wire
    def __init__(self):
        super().__init__(BIU.states)

        self.operand = False
        self.mem = True
        self.read = True

        # Registers
        self.IP = Register(16)
        self.FAR = Register(16)
        self.DR = Register(8)

        # Input/Output
        self.bus_data = Bus(8)

        # Output buses
        self.bus_data1 = Bus(8)
        self.bus_addr = Bus(16)

        # Input buses
        self.bus_addr1 = Bus(16)
        self.bus_data2 = Bus(16)

        # Output wires
        self.wire_instr_fetched = Wire(default=Wire.low_level)
        self.wire_operand_fetched = Wire(default=Wire.low_level)
        self.wire_is_wait = Wire(default=Wire.low_level)
        self.wire_output_enable = Wire(default=Wire.low_level)
        self.wire_data_enable = Wire(default=Wire.low_level)
        self.wire_MEM = Wire(default=Wire.high_level)
        self.wire_READ = Wire(default=Wire.high_level)

        # Input wires
        self.wire_direct_addr = Wire()
        self.wire_indirect_addr = Wire()
        self.wire_operand = Wire()
        self.wire_bit_depth0 = Wire()
        self.wire_bit_depth1 = Wire()
        self.wire_writable = Wire()
        self.wire_jump = Wire()
        self.wire_read = Wire()
        self.wire_mem = Wire()
        self.wire_ready = Wire(default=Wire.low_level)

        # Cycle managers
        self.__bfm = ByteFetchMng(self)
        self.__afm = AddrFetchMng(self)

    def phaseWait(self):
        self.__bfm.to_start()
        self.__afm.to_start()
        if self.wire_jump.is_high():
            self.IP.setInt(self.bus_addr1.get_value())
            self.set_state(self.stateByteFetch)
            self.operand = False
            self.read = True
            self.mem = True
            return False
        self.operand = self.wire_operand.is_high()
        self.read = self.wire_read.is_high()
        self.mem = self.wire_mem.is_high()
        if self.wire_indirect_addr.is_high() and self.wire_operand.is_low():
            self.set_state(BIU.stateAddrFetch)
        elif self.wire_operand.is_high() or self.wire_writable.is_high():
            self.set_state(BIU.stateByteFetch)
        return False

    def phaseByteFetch(self):
        if self.wire_jump.is_high():
            self.IP.setInt(self.bus_addr1.get_value())
            self.set_state(self.stateWait)
        else:
            self.__bfm.tick()
        return False

    def phaseAddrFetch(self):
        if self.wire_jump.is_high():
            self.IP.setInt(self.bus_addr1.get_value())
            self.set_state(self.stateWait)
        else:
            self.__afm.tick()
        return False

    def phaseJumpFetch(self):
        self.__jfm.tick()
        return False

    def stateToStr(self):
        state = ''
        if self.state == BIU.stateByteFetch.name:
            state = f'/{self.__bfm.state}'
        elif self.state == BIU.stateAddrFetch.name:
            state = f'/{self.__afm.state}'
        return f'State: {self.state}{state}'

    def __str__(self):
        state = ''
        if self.state == BIU.stateByteFetch.name:
            state = f'/{self.__bfm.state}'
        elif self.state == BIU.stateAddrFetch.name:
            state = f'/{self.__afm.state}'
        return f'''State: {self.state}{state}
IP:  {self.IP}
FAR: {self.FAR}
DR:  {self.DR}'''


class ByteFetchMng(CustomFSM):
    state0 = State('State0')
    state1 = State('State1')
    states = [
        state0,
        state1,
    ]

    def __init__(self, biu: BIU):
        super().__init__(ByteFetchMng.states)
        self.biu = biu
        self.DR = Register(32)

    def phaseState0(self):
        bias = (0b00 if self.biu.wire_bit_depth0.is_low() else 0b01) | (0b00 if self.biu.wire_bit_depth1.is_low() else 0b10)
        self.biu.wire_data_enable.set_high()
        self.biu.wire_MEM.set_level(self.biu.mem)
        self.biu.wire_READ.set_level(self.biu.read)

        if self.biu.operand:
            if self.biu.wire_direct_addr.is_high():
                self.biu.bus_addr.set_value(self.biu.bus_addr1.get_value() + bias)
            elif self.biu.wire_indirect_addr.is_high():
                self.biu.bus_addr.set_value(self.biu.FAR.getInt() + bias)
        else:
            self.biu.bus_addr.set_value(self.biu.IP.getInt())

        if not self.biu.read:
            self.biu.DR.setInt(self.biu.bus_data2.get_value())
            self.biu.bus_data.set_value(self.biu.DR.getInt())
        return True

    def phaseState1(self):
        # self.biu.DR.setInt(self.biu.memory.read())
        self.biu.wire_MEM.set_level(self.biu.mem)
        self.biu.wire_READ.set_level(self.biu.read)
        if not self.biu.mem:
            self.biu.bus_addr.set_value(self.biu.bus_addr1.get_value())
        if self.biu.wire_ready.is_high():
            if self.biu.read:
                self.biu.DR.setInt(self.biu.bus_data.get_value())
                self.biu.bus_data1.set_value(self.biu.DR.getInt())
                if not self.biu.operand:
                    self.biu.wire_instr_fetched.set_high()
                    self.biu.IP += 1
                else:
                    self.biu.wire_operand_fetched.set_high()
            else:
                if self.biu.operand:
                    self.biu.wire_operand_fetched.set_high()
            self.biu.wire_is_wait.set_high()
            self.biu.set_state(self.biu.stateWait)
        else:
            pass
            # self.biu.wire_data_enable.set_high()
        return False

class AddrFetchMng(CustomFSM):
    state0 = State('State0')
    state1 = State('State1')
    state2 = State('State2')
    state3 = State('State3')
    states = [
        state0,
        state1,
        state2,
        state3,
    ]

    def __init__(self, biu: BIU):
        super().__init__(AddrFetchMng.states)
        self.biu = biu
        self.DR = Register(32)

    def phaseState0(self):
        self.biu.wire_data_enable.set_high()
        self.biu.wire_MEM.set_high()
        self.biu.wire_READ.set_high()
        self.biu.bus_addr.set_value(self.biu.bus_addr1.get_value())
        return True

    def phaseState1(self):
        self.biu.wire_MEM.set_high()
        self.biu.wire_READ.set_high()
        if self.biu.wire_ready.is_high():
            self.biu.DR.setInt(self.biu.bus_data.get_value())
            self.biu.FAR.setInt(self.biu.DR.getInt() << 8)
            self.biu.wire_data_enable.set_high()
            self.biu.bus_addr.set_value(self.biu.bus_addr1.get_value() + 1)
            return True
        return False

    def phaseState2(self):
        self.biu.wire_data_enable.set_high()
        self.biu.wire_MEM.set_high()
        self.biu.wire_READ.set_high()
        if self.biu.wire_ready.is_high():
            self.biu.DR.setInt(self.biu.bus_data.get_value())
            self.biu.FAR.setInt(self.biu.FAR.getInt() | self.biu.DR.getInt())
            self.biu.wire_is_wait.set_high()
            self.biu.set_state(BIU.stateWait)
        return False
