def hex_to_str(value: int, length: int) -> str:
    value |= 0x10**length
    return f"0x{str(hex(value))[3:]}"


def hex_to_str_without_prefix(value: int, length: int) -> str:
    value |= 0x10**length
    return f"{str(hex(value))[3:]}"


def bin_to_str(value: int, length: int) -> str:
    value |= 0b10**length
    return f"0b{str(bin(value))[3:]}"


def binCmd8(value: int):
    value += 0x100
    return f"0b{str(bin(value))[3:8]}_{str(bin(value))[8:10]}_{str(bin(value))[10:]}"
