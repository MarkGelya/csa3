from hardware.base.register import Register


class Bus:
    def __init__(self, size, default=0b0):
        self.__size = size
        self.__default = default
        self.__value = Register(self.__size)
        self.__value.setInt(self.__default)
        self.__next = Register(self.__size)
        self.__next.setInt(self.__default)
        self.__is_new = False

    def reset(self):
        self.__value = self.__default

    def tick(self):
        self.__is_new = False
        self.__value.setInt(self.__next.getInt())
        self.__next.setInt(self.__default)

    def get_value(self):
        return self.__value.getInt()

    def set_value(self, value):
        self.__next.setInt(value)

    def __value_to_str(self, value):
        r = Register(self.__size)
        r.setInt(value)
        return str(r)

    def __str__(self):
        return f'{self.__value} -> {self.__next}, {self.__value_to_str(self.__default)}'
