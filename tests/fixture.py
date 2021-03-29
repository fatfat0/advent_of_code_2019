from helpers.opcode_computer import OpcodeComputer


def opcode(program_data):
    opcode_computer = OpcodeComputer()
    opcode_computer.run(program_data)
    return opcode_computer.get_results()
