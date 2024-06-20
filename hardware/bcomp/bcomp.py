import logging

from hardware.cpu.cpu import CPU
from hardware.devices.decimal_output import DecimalOutput
from hardware.devices.stream import Stream
from hardware.devices.terminal import Terminal
from hardware.memory.memory import Memory

logger = logging.getLogger(__name__)


class Bcomp:
    def __init__(self, input_filename):
        self.filename = input_filename
        self.cpu = CPU()
        self.mem = Memory()
        self.instr_num = 0
        self.tick_num = 0
        self.terminal = Terminal(self.filename)
        self.stream = Stream(self.filename)
        self.decimal_output = DecimalOutput()

        self.bus_data = self.cpu.bus_data
        self.bus_addr = self.cpu.bus_addr

        self.wire_ready = self.cpu.wires
        self.wire_hlt = self.cpu.eu.wire_hlt
        self.wire_read = self.cpu.wire_read
        self.wire_mem = self.cpu.wire_mem
        self.wire_instr = self.cpu.eu.wire_instr

    def tick(self):
        # _/¯
        self.cpu.tickUp()
        if self.cpu.wire_mem.is_high():
            if self.cpu.wire_data_enable.is_high():
                if self.cpu.wire_read.is_high():
                    self.mem.setAddr(self.cpu.bus_addr.get_value())
                    self.cpu.bus_data.set_value(self.mem.read())
                else:
                    self.mem.setAddr(self.cpu.bus_addr.get_value())
                    self.mem.write(self.cpu.bus_data.get_value())
                self.cpu.wire_ready.set_high()
        else:
            if self.cpu.bus_addr.get_value() == 0x0000:
                self.terminal.wire_data_enable.set_level(self.cpu.wire_data_enable.get_value())
                self.terminal.wire_read.set_level(self.cpu.wire_read.get_value())
                if self.cpu.wire_read.is_high():
                    self.bus_data.set_value(self.terminal.bus_data.get_value())
                else:
                    self.terminal.bus_data.set_value(self.bus_data.get_value())
                if self.terminal.wire_ready.is_high():
                    self.cpu.wire_ready.set_high()
            elif self.cpu.bus_addr.get_value() == 0x0001:
                self.stream.wire_data_enable.set_level(self.cpu.wire_data_enable.get_value())
                self.stream.wire_read.set_level(self.cpu.wire_read.get_value())
                if self.cpu.wire_read.is_high():
                    self.bus_data.set_value(self.stream.bus_data.get_value())
                else:
                    self.stream.bus_data.set_value(self.bus_data.get_value())
                if self.stream.wire_ready.is_high():
                    self.cpu.wire_ready.set_high()
                self.cpu.eu.flag_eof = self.stream.eof
            elif self.cpu.bus_addr.get_value() == 0x000A:
                self.decimal_output.wire_data_enable.set_level(self.cpu.wire_data_enable.get_value())
                self.decimal_output.wire_read.set_level(self.cpu.wire_read.get_value())
                if self.cpu.wire_read.is_low():
                    self.decimal_output.bus_data.set_value(self.bus_data.get_value())
                if self.decimal_output.wire_ready.is_high():
                    self.cpu.wire_ready.set_high()

        self.terminal.tick()
        self.stream.tick()
        self.decimal_output.tick()

        # ¯\_
        self.cpu.tick_down()
        self.tick_num += 1

    def instr(self):
        self.tick()
        if self.cpu.eu.wire_hlt.is_high():
            return
        while self.cpu.eu.wire_instr.is_low():
            self.tick()
            if self.cpu.eu.wire_hlt.is_high():
                return

        self.instr_num += 1

    def run(self, limit=1000000):
        while self.cpu.eu.wire_hlt.is_low():
            if self.tick_num > limit:
                raise ValueError(f"Tick limit {self.tick_num}")
            self.instr()

            logger.info(
                "\nUnits:"
                + "\nEU:\n" + str(self.cpu.eu)
                + "\nALU:\n" + str(self.cpu.eu.alu)
                + "\nIQ:\n" + str(self.cpu.iq)
                + "\nBIU:\n" + str(self.cpu.biu)
            )

            logger.debug(
                "\nWires:\n" + self.cpu.wire_to_str()
                + "\nBusses:\n" + self.cpu.busses_to_str()
            )

            if self.cpu.eu.wire_hlt.is_high():
                break
