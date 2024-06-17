import logging

from hardware.cpu.instructions.instructions import instrByOpCode
from hardware.cpu.interface_eu import InterfaceEU

logger = logging.getLogger(__name__)


class EU(InterfaceEU):
    def __init__(self):
        super().__init__()

    def phaseWait(self):
        return True

    def phaseInstructionFetch(self):
        if self.wire_instr_ready.is_high():
            self._CR.set_int(self.bus_instr.get_value())
            self.cmd = instrByOpCode(self._CR.get_int())(self, self._CR.get_int())
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
        cmd_state = ""
        if self.state == EU.stateExecution.name:
            if self.cmd:
                cmd_state = f"/{self.cmd.state}"
            else:
                cmd_state = "/CMD IS NONE"
        return f"State: {self.state}{cmd_state}"

    def __str__(self):
        cmd_state = ""
        if self.state == EU.stateExecution.name:
            if self.cmd:
                cmd_state = f"/{self.cmd.state}"
            else:
                cmd_state = "/CMD IS NONE"
        return f"""State: {self.state}{cmd_state}
CR: {self._CR} ({self.cmd})"""
