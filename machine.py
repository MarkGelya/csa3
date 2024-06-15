import logging
import sys

from hardware.bcomp.bcomp import Bcomp
from hardware.bios.bios import loadProgram
from hardware.cpu.biu import *
from hardware.cpu.cpu import CPU
from hardware.cpu.eu import EU

logging.basicConfig(
    level=logging.DEBUG,
)

loggers = ['transitions.core', 'asyncio']

for i in loggers:
    logging.getLogger(i).setLevel(logging.ERROR)

def main(code_filename: str, input_filename: str):
    f = open(code_filename, 'rb')
    data = f.read()
    f.close()
    bcomp = Bcomp(input_filename)
    loadProgram(bcomp.mem, data)

    bcomp.run()



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])