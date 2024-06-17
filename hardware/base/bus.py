from hardware.base.register import Register


class Bus:
    def __init__(self, size, default=0b0):
        self.__size = size
        self.__default = default
        self.__value = Register(self.__size)
        self.__value.set_int(self.__default)
        self.__next = Register(self.__size)
        self.__next.set_int(self.__default)
        self.__is_new = False

    def reset(self):
        self.__value = self.__default

    def tick(self):
        self.__is_new = False
        self.__value.set_int(self.__next.get_int())
        self.__next.set_int(self.__default)

    def get_value(self):
        return self.__value.get_int()

    def set_value(self, value):
        self.__next.set_int(value)

    def __value_to_str(self, value):
        r = Register(self.__size)
        r.set_int(value)
        return str(r)

    def __str__(self):
        return f"{self.__value} -> {self.__next}, {self.__value_to_str(self.__default)}"
