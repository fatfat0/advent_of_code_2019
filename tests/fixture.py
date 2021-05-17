from helpers.opcode_computer import OpcodeComputer


def opcode(program_data, computer_inputs=[]):
    opcode_computer = OpcodeComputer()
    opcode_computer.run(program=program_data, computer_inputs=computer_inputs)
    return opcode_computer.get_results()


def opcode_output(program_data, computer_inputs=[]):
    opcode_computer = OpcodeComputer()
    opcode_computer.run(program=program_data, computer_inputs=computer_inputs)
    return opcode_computer.diagnostic_output()
