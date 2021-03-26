from helpers.opcode_computer import OpcodeComputer


def opcode(program_data):
    opcode_computer = OpcodeComputer(program_data)
    opcode_computer.run()
    return opcode_computer.get_results()


def test_cases_part_1():
    """Example data in the problem"""
    assert opcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [
        3500,
        9,
        10,
        70,
        2,
        3,
        11,
        0,
        99,
        30,
        40,
        50,
    ]
    assert opcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert opcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert opcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert opcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
