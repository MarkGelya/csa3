from hardware.memory.memory import Memory


def load_program(mem: Memory, data: bytes):
    for i in range(len(data)):
        mem.setAddr(i)
        mem.write(data[i])
