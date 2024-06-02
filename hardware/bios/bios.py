from hardware.memory.memory import Memory

def loadProgram(mem: Memory, data: bytes):
    for i in range(len(data)):
        mem.setAddr(i)
        mem.write(data[i])
