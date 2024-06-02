import logging

from hardware.cpu.interface_eu import InterfaceEU
from hardware.cpu.instructions.instructions import instrByOpCode

logger = logging.getLogger(__name__)

class EU(InterfaceEU):
    def __init__(self):
        super().__init__()

    def phaseWait(self):
        return True

    def phaseInstructionFetch(self):
        if self.wire_instr_ready.is_high():
            self._CR.setInt(self.bus_instr.get_value())
            self.cmd = instrByOpCode(self._CR.getInt())(self, self._CR.getInt())
            self.wire_skip.set_high()
            return True
        return False

    def phaseExecution(self):
        self.cmd.tick()
        return False

    def phaseHlt(self):
        self.wire_hlt.set_high()
        if self.wire_run.is_high():
            self.set_state(InterfaceEU.stateInstrFetch)
        return False

    def stateToStr(self):
        cmdState = ''
        if self.state == EU.stateExecution.name:
            if self.cmd:
                cmdState = f'/{self.cmd.state}'
            else:
                cmdState = f'/CMD IS NONE'
        return f'State: {self.state}{cmdState}'

    def __str__(self):
        cmdState = ''
        if self.state == EU.stateExecution.name:
            if self.cmd:
                cmdState = f'/{self.cmd.state}'
            else:
                cmdState = f'/CMD IS NONE'
        return f'''State: {self.state}{cmdState}
CR: {self._CR} ({self.cmd})'''
