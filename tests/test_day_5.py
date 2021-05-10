from fixture import opcode


def test_modes_part_1():
    assert opcode(program_data=[1002, 4, 3, 4, 33], computer_input=1) == [
        1002,
        4,
        3,
        4,
        99,
    ]
    assert opcode(program_data=[1101, 100, -1, 4, 0], computer_input=1) == [
        1101,
        100,
        -1,
        4,
        99,
    ]
