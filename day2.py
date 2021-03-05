from itertools import product

from helpers.opcode_computer import OpcodeComputer
from helpers.data_access import get_data

data = get_data(day=2)

# Part 1


# Tests for part one. Uncomment any program_master line to run test.
# program_master = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]  # answer should be 3500
# program_master = [1, 0, 0, 0, 99]  # answer should be 2
# program_master = [2, 3, 0, 3, 99]  # answer should be 2
# program_master = [2, 4, 4, 5, 99, 0]  # answer should be 2
program_master = [99]  # answer should be 30
computer = OpcodeComputer(list(program_master))
computer.run()
print(f"Test value left at position 0 is {computer[0]}")

program_master = [int(entry) for entry in data.split(",")]

computer = OpcodeComputer(list(program_master))
computer.set_inputs([12, 2])
computer.run()

print(f"Value left at position 0 is {computer[0]}")

# Part 2

for noun, verb in product(range(1, 100), repeat=2):
    computer = OpcodeComputer(list(program_master))
    computer.set_inputs([noun, verb])
    computer.run()

    if computer.output == 19690720:
        break

print(f"Correct output provided by {noun}, {verb}, with key {100*noun+verb}")
