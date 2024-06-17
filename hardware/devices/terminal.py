from hardware.base.bus import Bus
from hardware.base.wire import Wire


class Terminal:
    def __init__(self, filename=None):
        self.counter = 0
        self.tick_on_work = 6
        self.is_work = False
        # self.addr = 0
        self.data = 0
        # self.addr_enable = False
        self.read = False

        # From terminal to device
        if filename:
            with open(filename, mode="rb") as f:
                data = bytearray(f.read())[:255]
                self.output_buff = bytearray([len(data)]) + data
        else:
            self.output_buff = bytearray(255)
        self.output_pointer = 0

        # From device to terminal
        self.input_buff = bytearray(255)
        self.input_pointer = 0

        # Input/Output
        self.bus_data = Bus(8)

        # Output
        self.wire_ready = Wire(default=Wire.low_level)

        # Input
        self.wire_data_enable = Wire(default=Wire.low_level)
        self.wire_read = Wire(default=Wire.low_level)

    def tick(self):
        self.bus_data.tick()
        self.wire_ready.tick()
        self.wire_data_enable.tick()
        self.wire_read.tick()
        if self.is_work:
            if self.counter >= self.tick_on_work:
                if self.read:
                    if (self.output_pointer > self.output_buff[0]) or (self.output_buff[0] == 0):
                        self.input()
                    elif self.output_pointer == 0:
                        print(f"< {self.output_buff[1:self.output_buff[0]+1].decode('ASCII')}")
                    self.bus_data.set_value(self.output_buff[self.output_pointer % 256])
                    self.output_pointer += 1
                else:
                    self.input_buff[self.input_pointer % 256] = self.data
                    if self.input_pointer >= self.input_buff[0]:
                        self.print()
                        self.input_pointer = 0
                    else:
                        self.input_pointer += 1
                self.wire_ready.set_high()
                self.counter = 0
                self.is_work = False
            else:
                self.counter += 1
        else:
            # if self.wire_addr_enable.is_high():
            #     self.addr = self.bus_addr.get_value()
            #     self.addr_enable = True
            if self.wire_data_enable.is_high():
                self.data = self.bus_data.get_value()
                self.read = self.wire_read.is_high()
                self.is_work = True

    def input(self):
        s = input("< ")
        self.output_pointer = 0
        self.output_buff = (bytearray([len(s)]) if len(s) < 256 else bytearray([0xFF])) + s.encode("ASCII")[:256]

    def input_from_file(self, filename):
        f = open(filename, "rb")
        data = f.read()
        f.close()
        self.output_buff = (bytearray([len(data)]) if len(data) < 256 else bytearray([0xFF])) + data[:256]

    def print(self):
        print(f"> {self.input_buff[1:self.input_buff[0]+1].decode('ASCII')}")

    def __str__(self):
        return f"""addr enable: {self.wire_data_enable}
read       : {self.wire_read}
mem        : {self.wire_mem}
ready      : {self.wire_ready}
bus data   : {self.bus_data}
"""
