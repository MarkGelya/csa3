from hardware.base.register import Register
from utils.formatters import hexToStrWithoutPrefix, hexToStr


class Memory:
    def __init__(self):
        self._data = bytearray(2**16)
        self._AR = 0

    def setAddr(self, value):
        self._AR = value

    def read(self):
        return self._data[self._AR]

    def write(self, value):
        self._data[self._AR] = value

    def toStr(self, line_size=4, begin_line=0, end_line=10):
        res = f'AR: {hexToStr(self._AR, 4)}\n'
        for i in range(begin_line, end_line+1):
            # res += f'{str(i).rjust(len(str(end_line)))}: '
            res += f'{str(hexToStr(i * line_size, len(hex(end_line * line_size)))).rjust(len(hex(end_line * line_size)))}: '
            for j in range(line_size):
                res += hexToStrWithoutPrefix(self._data[i * line_size + j], 2) + ' '
            if i != end_line:
                res += '\n'
        return res

