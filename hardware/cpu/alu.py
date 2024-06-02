from hardware.base.register import Register
from hardware.cpu.flags import Flags
from utils.formatters import hexToStr


class ALU32:
    def __init__(self):
        self.__A = Register(size=32)
        self.__B = Register(size=32)
        self.flags_CF = 0
        self.flags_OF = 0
        self.flags_NF = 0
        self.flags_ZF = 1
        
    def __update_flags(self):
        self.flags_NF = 1 if self.__A[len(self.__A) - 1] < 0 else 0
        self.flags_ZF = 1 if self.__A.getInt() == 0 else 0

    def update_flags(self):
        self.__update_flags()

    def __bitwise_add(self):
        result = Register(32)
        carry = 0
        c = 0
        for i in range(len(self.__A)):
            sum_bit = self.__A[i] ^ self.__B[i] ^ carry
            carry = 1 if (self.__A[i] + self.__B[i] + carry) > 1 else 0
            result[i] = sum_bit
            if i == len(self.__A) - 2:
                c = carry
        self.flags_CF = carry
        self.flags_OF = c ^ carry
        self.flags_NF = result[len(self.__A) - 1]
        self.flags_ZF = 1 if result.getInt() == 0 else 0
        return result.getInt()

    def __bitwise_sub(self):
        result = Register(32)
        carry = 0
        c = 0
        for i in range(len(self.__A)):
            diff_bit = self.__A[i] ^ self.__B[i] ^ carry
            carry = 1 if (self.__A[i] - self.__B[i] - carry) < 0 else 0
            result[i] = diff_bit
            if i == len(self.__A) - 2:
                c = carry
        self.flags_CF = carry
        self.flags_OF = c ^ carry
        self.flags_NF = result[len(self.__A) - 1]
        self.flags_ZF = 1 if result.getInt() == 0 else 0
        return result.getInt()

    def set_a(self, value: int):
        self.__A.setInt(value)
        self.__update_flags()

    def set_b(self, value: int):
        self.__B.setInt(value)

    def get_a(self) -> int:
        return self.__A.getInt()

    def get_a_reg(self) -> Register:
        return self.__A

    def get_b(self):
        return self.__B.getInt()

    def get_b_reg(self) -> Register:
        return self.__B

    def ADD(self):
        self.__A.setInt(self.__bitwise_add())

    def SUB(self):
        self.__A.setInt(self.__bitwise_sub())

    def NOT(self):
        self.__A.setInt(self.__A.getInt() ^ 0xFFFFFFFF)
        self.__update_flags()

    def XOR(self):
        self.__A.setInt(self.__A.getInt() ^ self.__B.getInt())
        self.__update_flags()

    def AND(self):
        self.__A.setInt(self.__A.getInt() & self.__B.getInt())
        self.__update_flags()

    def OR(self):
        self.__A.setInt(self.__A.getInt() | self.__B.getInt())
        self.__update_flags()

    def DEC(self):
        self.__A.setInt(self.__A.getInt() - 1)
        self.__update_flags()

    def INC(self):
        self.__A.setInt(self.__A.getInt() + 1)
        self.__update_flags()

    def CMP(self):
        self.__bitwise_sub()

    def __str__(self):
        return f"""A: {self.__A} {hexToStr(self.__A.getInt(), 8)}
B: {self.__B} {hexToStr(self.__B.getInt(), 8)}
CF: {self.flags_CF} OF: {self.flags_OF} ZF: {self.flags_ZF} NF: {self.flags_NF}"""