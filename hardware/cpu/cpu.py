from hardware.cpu.biu import BIU
from hardware.cpu.eu import EU
from hardware.cpu.instr_queue import InstructionQueue


class CPU:
    def __init__(self):
        self.tick_num = 0
        self.instr_num = 0

        self.iq = InstructionQueue()
        self.biu = BIU()
        self.eu = EU()

        self.wire_data_enable = self.biu.wire_data_enable
        self.bus_addr = self.biu.bus_addr
        self.bus_data = self.biu.bus_data
        self.wire_ready = self.biu.wire_ready
        self.wire_read = self.biu.wire_READ
        self.wire_mem = self.biu.wire_MEM

        self.biu.wire_operand = self.eu.wire_operand
        self.biu.wire_mem = self.eu.wire_mem
        self.biu.wire_read = self.eu.wire_read
        self.biu.wire_direct_addr = self.eu.wire_direct_addr
        self.biu.wire_indirect_addr = self.eu.wire_indirect_addr
        self.biu.wire_bit_depth0 = self.eu.wire_bit_depth0
        self.biu.wire_bit_depth1 = self.eu.wire_bit_depth1
        self.biu.wire_writable = self.iq.wire_writable
        self.biu.bus_addr1 = self.iq.bus_addr1
        self.biu.wire_jump = self.eu.wire_jump
        self.biu.wire_read = self.eu.wire_read
        self.biu.bus_data2 = self.eu.bus_data2

        self.eu.wire_instr_ready = self.iq.wire_instr_ready
        self.eu.wire_addr_ready = self.iq.wire_addr_ready
        self.eu.wire_operand_fetched = self.biu.wire_operand_fetched
        self.eu.wire_biu_is_wait = self.biu.wire_is_wait
        self.eu.bus_instr = self.iq.bus_instr
        self.eu.bus_data1 = self.biu.bus_data1

        self.iq.wire_drop = self.eu.wire_drop
        self.iq.wire_skip = self.eu.wire_skip
        self.iq.wire_skip_addr = self.eu.wire_skip_addr
        self.iq.wire_instr_fetched = self.biu.wire_instr_fetched
        self.iq.bus_data = self.biu.bus_data1

        self.wires = {
            "operand": self.eu.wire_operand,
            "direct addr": self.eu.wire_direct_addr,
            "indirect addr": self.eu.wire_indirect_addr,
            "bit depth0": self.eu.wire_bit_depth0,
            "bit depth1": self.eu.wire_bit_depth1,
            "jump": self.eu.wire_jump,
            "drop": self.eu.wire_drop,
            "skip": self.eu.wire_skip,
            "skip addr": self.eu.wire_skip_addr,
            "read": self.eu.wire_read,
            "mem": self.eu.wire_mem,
            "hlt": self.eu.wire_hlt,
            "run": self.eu.wire_run,
            "instr": self.eu.wire_instr,
            "operand fetched": self.biu.wire_operand_fetched,
            "instr fetched": self.biu.wire_instr_fetched,
            "biu is wait": self.biu.wire_is_wait,
            "output enable": self.biu.wire_output_enable,
            "instr ready": self.iq.wire_instr_ready,
            "addr ready": self.iq.wire_addr_ready,
            "writable": self.iq.wire_writable,
            "DEN": self.biu.wire_data_enable,
            "READY": self.biu.wire_ready,
            "MEM": self.wire_mem,
            "READ": self.wire_read,
        }

        self.buses = {
            "data1": self.biu.bus_data1,
            "data2": self.biu.bus_data2,
            "instr": self.iq.bus_instr,
            "addr1": self.iq.bus_addr1,
            "DATA": self.biu.bus_data,
            "ADDR": self.biu.bus_addr,
        }

    def tick_wires(self):
        for key, value in self.wires.items():
            value.tick()

    def tick_buses(self):
        for key, value in self.buses.items():
            value.tick()

    def wire_to_str(self):
        res = list()
        for key, value in self.wires.items():
            res.append(f"{key.ljust(15)}: {value}")
        return "\n".join(res)

    def busses_to_str(self):
        res = list()
        for key, value in self.buses.items():
            res.append(f"{key.ljust(5)}: {value}")
        return "\n".join(res)

    # _/¯
    def tickUp(self):
        self.tick_num += 1
        self.biu.tick()
        self.iq.tick()
        self.eu.tick()

    # ¯\_
    def tick_down(self):
        self.tick_wires()
        self.tick_buses()

    def tick(self):
        self.tickUp()
        self.tick_down()
        # print(f'tick number: {self.tick_num}')

    def instr(self):
        self.tick()
        while self.eu.wire_instr.is_low():
            self.tick()
        self.instr_num += 1
        # logger.info(
        #     f'\n        ALU:\n{self.eu.alu}\n        EU:\n{self.eu}\n        IQ:\n{self.iq}\n        BIU:\n{self.biu}'
        # )
        # logger.info(f'instructions: {self.instr_num}, ticks: {self.tick_num}')

    def run_instr(self, limit=50000):
        # logger.info(
        #     f'\n        ALU:\n{self.eu.alu}\n        EU:\n{self.eu}\n        IQ:\n{self.iq}\n        BIU:\n{self.biu}'
        # )
        # logger.info(f'instructions: {self.instr_num}, ticks: {self.tick_num}')
        while self.eu.wire_hlt.is_low():
            if self.tick_num > limit:
                raise ValueError(f"Tick limit {self.tick_num}")
            self.tick()
