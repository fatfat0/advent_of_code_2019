from itertools import product

from helpers.opcode_computer import OpcodeComputer
from helpers.data_access import get_data

data = get_data(day=5)

# Part 1

program_master = [int(entry) for entry in data.split(",")]
computer = OpcodeComputer(list(program_master))
computer.run()

# Part 2