from utils.formatters import hex_to_str, hex_to_str_without_prefix


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
        res = f"AR: {hex_to_str(self._AR, 4)}\n"
        for i in range(begin_line, end_line + 1):
            # res += f'{str(i).rjust(len(str(end_line)))}: '
            res += f"{str(hex_to_str(i * line_size, len(hex(end_line * line_size)))).rjust(len(hex(end_line * line_size)))}: "
            for j in range(line_size):
                res += hex_to_str_without_prefix(self._data[i * line_size + j], 2) + " "
            if i != end_line:
                res += "\n"
        return res
