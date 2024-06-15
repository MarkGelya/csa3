from hardware.base.bus import Bus
from hardware.base.wire import Wire


class Stream:
    def __init__(self, filename):
        self.counter = 0
        self.tick_on_work = 6
        self.is_work = False
        # self.addr = 0
        self.data = 0
        # self.addr_enable = False
        self.read = False

        # Flags
        self.eof = False

        # From stream to device
        self.output_pointer = 0
        self.output_buff = bytearray([0])
        with open(filename, mode="rb") as f:
            self.output_buff = f.read()

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
                    if self.output_pointer < len(self.output_buff):
                        self.bus_data.set_value(self.output_buff[self.output_pointer])
                        self.output_pointer += 1
                    else:
                        self.eof = True
                else:
                    print(str(bytes([self.data]))[2:-1], end='')
                self.wire_ready.set_high()
                self.counter = 0
                self.is_work = False
            else:
                self.counter += 1
        else:
            if self.wire_data_enable.is_high():
                self.data = self.bus_data.get_value()
                self.read = self.wire_read.is_high()
                self.is_work = True

    def __str__(self):
        return f'''addr enable: {self.wire_data_enable}
read       : {self.wire_read}
mem        : {self.wire_mem}
ready      : {self.wire_ready}
bus data   : {self.bus_data}
'''
