def hexToStr(value: int, len: int) -> str:
    value |= 0x10**len
    return f'0x{str(hex(value))[3:]}'

def hexToStrWithoutPrefix(value: int, len: int) -> str:
    value |= 0x10**len
    return f'{str(hex(value))[3:]}'

def binToStr(value: int, len: int) -> str:
    value |= 0b10**len
    return f'0b{str(bin(value))[3:]}'

def binCmd8(value: int):
    value += 0x100
    return f'0b{str(bin(value))[3:8]}_{str(bin(value))[8:10]}_{str(bin(value))[10:]}'