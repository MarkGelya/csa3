from hardware.base.register import Register


class Flags(Register):
    def __init__(self):
        super().__init__(32)

    @property
    def NF(self):
        return self[3]

    @NF.setter
    def NF(self, value):
        self[3] = value

    @property
    def ZF(self):
        return self[2]

    @ZF.setter
    def ZF(self, value):
        self[2] = value

    @property
    def OF(self):
        return self[1]

    @OF.setter
    def OF(self, value):
        self[1] = value

    @property
    def CF(self):
        return self[0]

    @CF.setter
    def CF(self, value):
        self[0] = value
