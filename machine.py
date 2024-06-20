import logging
import sys

from hardware.bcomp.bcomp import Bcomp
from hardware.bios.bios import load_program

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
)

loggers = ["transitions.core", "asyncio"]

for i in loggers:
    logging.getLogger(i).setLevel(logging.WARNING)


def main(code_filename: str, input_filename: str):
    f = open(code_filename, "rb")
    data = f.read()
    f.close()
    bcomp = Bcomp(input_filename)
    load_program(bcomp.mem, data)
    bcomp.run()
    logger.info(
        f"instr_counter: {bcomp.instr_num} ticks: {bcomp.tick_num}"
    )


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
