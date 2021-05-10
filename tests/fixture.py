from helpers.opcode_computer import OpcodeComputer


def opcode(program_data, computer_input=None):
    opcode_computer = OpcodeComputer()
    opcode_computer.run(program=program_data, computer_input=computer_input)
    return opcode_computer.get_results()
