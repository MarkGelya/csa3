from hardware.cpu.cpu import CPU
from hardware.devices.stream import Stream
from hardware.devices.terminal import Terminal
from hardware.memory.memory import Memory

class Bcomp:
    def __init__(self, input_filename):
        self.filename = input_filename
        self.cpu = CPU()
        self.mem = Memory()
        self.instr_num = 0
        self.tick_num = 0
        self.terminal = Terminal(self.filename)
        self.stream = Stream(self.filename)

        self.bus_data = self.cpu.bus_data
        self.bus_addr = self.cpu.bus_addr

        self.wire_ready = self.cpu.wires
        # self.wire_hlt = self.cpu.wire_hlt
        self.wire_read = self.cpu.wire_read
        self.wire_mem = self.cpu.wire_mem
        # self.wire_instr = self.cpu.wire_instr

    def tick(self):
        # _/¯
        self.cpu.tickUp()

        # print(self.cpu.eu.alu)
        # print()
        # print(self.cpu.eu)
        # print()
        # print(self.cpu.iq)
        # print()
        # print(self.cpu.biu)

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

        self.terminal.tick()
        self.stream.tick()

        # ¯\_
        self.cpu.tickDown()

        # self.cpu.printWire()
        # print()
        # self.cpu.printBuses()
        # print()

        self.tick_num += 1
        # print(f'tick: {self.tick_num}')

    def instr(self):
        self.tick()
        while self.cpu.eu.wire_instr.is_low():
            self.tick()
        self.instr_num += 1
        # print(self.cpu.eu.alu)
        # print()
        # print(self.cpu.eu)
        # print()
        # print(self.cpu.iq)
        # print()
        # print(self.cpu.biu)
        # print()
        # print(f'tick: {self.tick_num}')

    def run(self, limit=50000):
        counter = 0
        while self.cpu.eu.wire_hlt.is_low():
            if self.tick_num > limit:
                raise ValueError(f'Tick limit {self.tick_num}')
            self.tick()
