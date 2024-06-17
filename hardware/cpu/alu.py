from hardware.base.register import Register
from utils.formatters import hex_to_str


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
        self.flags_ZF = 1 if self.__A.get_int() == 0 else 0

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
        self.flags_ZF = 1 if result.get_int() == 0 else 0
        return result.get_int()

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
        self.flags_ZF = 1 if result.get_int() == 0 else 0
        return result.get_int()

    def set_a(self, value: int):
        self.__A.set_int(value)
        self.__update_flags()

    def set_b(self, value: int):
        self.__B.set_int(value)

    def get_a(self) -> int:
        return self.__A.get_int()

    def get_a_reg(self) -> Register:
        return self.__A

    def get_b(self):
        return self.__B.get_int()

    def get_b_reg(self) -> Register:
        return self.__B

    def ADD(self):
        self.__A.set_int(self.__bitwise_add())

    def SUB(self):
        self.__A.set_int(self.__bitwise_sub())

    def NOT(self):
        self.__A.set_int(self.__A.get_int() ^ 0xFFFFFFFF)
        self.__update_flags()

    def XOR(self):
        self.__A.set_int(self.__A.get_int() ^ self.__B.get_int())
        self.__update_flags()

    def AND(self):
        self.__A.set_int(self.__A.get_int() & self.__B.get_int())
        self.__update_flags()

    def OR(self):
        self.__A.set_int(self.__A.get_int() | self.__B.get_int())
        self.__update_flags()

    def DEC(self):
        self.__A.set_int(self.__A.get_int() - 1)
        self.__update_flags()

    def INC(self):
        self.__A.set_int(self.__A.get_int() + 1)
        self.__update_flags()

    def CMP(self):
        self.__bitwise_sub()

    def __str__(self):
        return f"""A: {self.__A} {hex_to_str(self.__A.get_int(), 8)}
B: {self.__B} {hex_to_str(self.__B.get_int(), 8)}
CF: {self.flags_CF} OF: {self.flags_OF} ZF: {self.flags_ZF} NF: {self.flags_NF}"""
