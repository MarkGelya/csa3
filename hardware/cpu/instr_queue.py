from hardware.base.bus import Bus
from hardware.base.register import Register
from hardware.base.wire import Wire


class InstructionQueue:
    def __init__(self):
        self.queue = list()
        self.maxsize = 4
        for i in range(self.maxsize):
            self.queue.append(Register(8))
        self.write_pointer = 0
        self.read_pointer = 0
        self.size = 0

        # Output buses
        self.bus_addr1 = Bus(16)
        self.bus_instr = Bus(8)

        # Input buses
        self.bus_data = Bus(8)

        # Output wires
        self.wire_instr_ready = Wire(default=Wire.low_level)
        self.wire_addr_ready = Wire(default=Wire.low_level)
        self.wire_writable = Wire(default=Wire.high_level)
        self.wire_fetched = Wire(default=Wire.low_level)

        # Input wires
        self.wire_drop = Wire()
        self.wire_instr_fetched = Wire()
        self.wire_skip = Wire()
        self.wire_skip_addr = Wire()

    def tick(self):
        if self.wire_drop.is_high():
            self.drop()
        else:
            if self.wire_instr_fetched.is_high():
                self.write(self.bus_data.get_value())
            if self.wire_skip_addr.is_high():
                self.double_skip()
            elif self.wire_skip.is_high():
                self.skip()
        self.wire_instr_ready.set_level(self.is_readable())
        self.wire_addr_ready.set_level(self.is_readable_addr())
        self.wire_writable.set_level(self.is_writable())
        self.bus_instr.set_value(self.read())
        self.bus_addr1.set_value(self.readAddr())

    def empty(self):
        return self.size == 0

    def isEmptyAddr(self):
        return self.size < 2

    def full(self):
        return self.size == self.maxsize

    def read(self) -> int:
        # if self.empty():
        #     raise ValueError('Connot read. Queue is empty.')
        res = self.queue[self.read_pointer]
        return res.get_int()

    def write(self, value):
        if self.full():
            raise ValueError("Connot write. Queue is full.")
        self.size += 1
        if isinstance(value, int):
            self.queue[self.write_pointer].set_int(value)
        elif isinstance(value, Register):
            self.queue[self.write_pointer].set_int(value.get_int())
        else:
            raise TypeError("Expected 'int' or 'Register'.")
        self.write_pointer = (self.write_pointer + 1) % self.maxsize

    def skip(self):
        if self.empty():
            raise ValueError("Connot skip. Queue is empty.")
        self.size -= 1
        self.read_pointer = (self.read_pointer + 1) % self.maxsize

    def double_skip(self):
        self.skip()
        self.skip()

    def drop(self):
        self.size = 0
        self.write_pointer = 0
        self.read_pointer = 0

    def is_writable(self) -> bool:
        return self.maxsize - self.size >= 1

    def is_writable_addr(self) -> bool:
        return self.maxsize - self.size >= 2

    def is_readable(self) -> bool:
        return self.size >= 1

    def is_readable_addr(self) -> bool:
        return self.size >= 3  # instr + addr

    def readAddr(self) -> int:
        # if self.isEmptyAddr():
        #     raise ValueError('Connot read addres.')
        res = Register(16)
        res.set_int(
            (self.queue[self.read_pointer].get_int() << 8)
            + self.queue[(self.read_pointer + 1) % self.maxsize].get_int()
        )
        return res.get_int()

    def __str__(self):
        res = list()
        for i in range(self.maxsize):
            res.append(
                f" {'<-' if i == self.read_pointer else '  '} {self.queue[i]} {'<-' if i == self.write_pointer else '  '}"
            )
        return "\n".join(res)
