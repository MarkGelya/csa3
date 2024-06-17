from hardware.base.bus import Bus
from hardware.base.wire import Wire


class DecimalOutput:
    def __init__(self):
        self.counter = 0
        self.tick_on_work = 6
        self.is_work = False
        # self.addr = 0
        self.data = 0
        # self.addr_enable = False
        self.read = False

        # From device to terminal
        self.input_buff = bytearray(4)
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
                if not self.read:
                    self.input_buff[self.input_pointer] = self.data
                    if self.input_pointer == 3:
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
            if self.wire_data_enable.is_high():
                self.data = self.bus_data.get_value()
                self.read = self.wire_read.is_high()
                self.is_work = True

    def print(self):
        print(f"> {int.from_bytes(self.input_buff)}")

    def __str__(self):
        return f"""addr enable: {self.wire_data_enable}
read       : {self.wire_read}
mem        : {self.wire_mem}
ready      : {self.wire_ready}
bus data   : {self.bus_data}
"""
