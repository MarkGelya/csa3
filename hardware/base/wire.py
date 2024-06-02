

class Wire:
    unset_level = -1
    low_level = 0
    high_level = 1

    def __init__(self, default=unset_level):
        self.__default = default
        self.__value = self.__default
        self.__next = self.__default
        self.__is_new = False

    def reset(self):
        self.__value = self.__default
        self.__next = self.__next
    def tick(self):
        self.__is_new = False
        self.__value = self.__next
        self.__next = self.__default

    def set_high(self):
        if self.__is_new:
            raise ValueError('The value is already set.')
        self.__is_new = True
        self.__next = self.high_level

    def set_low(self):
        if self.__is_new:
            raise ValueError('The value is already set.')
        self.__is_new = True
        self.__next = self.low_level

    def get_value(self):
        if self.__value == self.unset_level:
            raise ValueError('The value is not set.')
        return self.__value == self.high_level

    def is_high(self):
        return self.get_value() == self.high_level

    def is_low(self):
        return self.get_value() == self.low_level

    def set_level(self, value):
        if type(value) is int:
            self.__next = self.high_level if value != 0 else self.low_level
        if type(value) is bool:
            self.__next = self.high_level if value else self.low_level

    def __value_to_str(self, value):
        if value == self.low_level:
            return '0'
        elif value == self.high_level:
            return '1'
        else:
            return '_'

    def __str__(self):
        return f'{self.__value_to_str(self.__value)} -> {self.__value_to_str(self.__next)}, {self.__value_to_str(self.__default)}'
