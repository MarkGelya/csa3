from utils.formatters import *


class Register:
    def __init__(self, size=32):
        self._value = 0
        self._size = size
        self.mask = (1 << size) - 1

    def __setitem__(self, index, value):
        if index < self._size:
            self._value |= (value << index)
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
        return binToStr(self.getInt(), len(self))

    def __add__(self, other):
        self._value = (self._value + other) & self.mask
        return self

    def setInt(self, value):
        if isinstance(value, int):
            if value < 0:
                self._value = (abs(value) ^ self.mask) + 1
            else:
                self._value = value
        elif isinstance(value, Register):
            self.setInt(value.getInt())
        else:
            raise ValueError("Except 'int' or 'Register'")

    def getInt(self):
        return self._value
