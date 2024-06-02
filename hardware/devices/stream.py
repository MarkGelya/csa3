from hardware.base.bus import Bus
from hardware.base.wire import Wire


class Stream:
    def __init__(self):
        self.counter = 0
        self.tick_on_work = 6
        self.is_work = False
        # self.addr = 0
        self.data = 0
        # self.addr_enable = False
        self.data_enable = False
        self.read = False
        self.buff = bytearray(255)
        self.pointer = 0

        # Input/Output
        self.bus_data = Bus(8)

        # Output
        self.wire_ready = Wire(default=Wire.low_level)

        # Input
        self.wire_data_enable = Wire(default=Wire.low_level)
        self.wire_read = Wire(default=Wire.low_level)
        self.wire_mem = Wire(default=Wire.low_level)

    def tick(self):
        if self.is_work:
            if self.counter >= self.tick_on_work:
                if self.read:
                    self.bus_data.set_value(self.buff[self.pointer % 256])
                    self.pointer += 1
                else:
                    self.buff[self.pointer % 256] = self.bus_data.get_value()
                    self.pointer += 1
                    print(self.data)
                self.wire_ready.set_high()
                self.counter = 0
                self.is_work = False
                # self.addr_enable = False
                self.data_enable = False
            else:
                self.counter += 1
        else:
            # if self.wire_addr_enable.is_high():
            #     self.addr = self.bus_addr.get_value()
            #     self.addr_enable = True
            if self.wire_data_enable.is_high():
                self.data = self.bus_data.get_value()
                self.data_enable = True
                self.read = self.wire_read.is_high()
            self.is_work = self.data_enable

    def input(self):
        s = input()
        self.buff = (bytearray([len(s)]) if len(s) < 256 else bytearray([0xFF])) + s.encode('ASCII')[:255]

    def output(self):
        print(self.buff[1:self.buff[0]].decode('ASCII'))

    def __str__(self):
        return f'''addr enable: {self.wire_data_enable}
read       : {self.wire_read}
mem        : {self.wire_mem}
ready      : {self.wire_ready}
bus data   : {self.bus_data}
'''
