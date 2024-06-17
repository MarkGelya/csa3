from utils.formatters import bin_to_str


class Register:
    def __init__(self, size=32):
        self._value = 0
        self._size = size
        self.mask = (1 << size) - 1

    def __setitem__(self, index, value):
        if index < self._size:
            self._value |= value << index
        else:
            raise IndexError(f"Bit index '{index}' out of range '{self._size}'.")

    def __getitem__(self, index):
        if index < self._size:
            return (self._value >> index) & 1
        else:
            raise IndexError(f"Bit index '{index}' out of range '{self._size}'.")

    def __len__(self):
        return self._size

    def __str__(self):
        return bin_to_str(self.get_int(), len(self))

    def __add__(self, other):
        self._value = (self._value + other) & self.mask
        return self

    def set_int(self, value):
        if isinstance(value, int):
            if value < 0:
                self._value = (abs(value) ^ self.mask) + 1
            else:
                self._value = value
        elif isinstance(value, Register):
            self.set_int(value.get_int())
        else:
            raise ValueError("Except 'int' or 'Register'")

    def get_int(self):
        return self._value
