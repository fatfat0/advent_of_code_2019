from fixture import opcode


def test_modes_part_1():
    assert opcode([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]
    assert opcode([1101, 100, -1, 4, 0]) == [1101, 100, -1, 4, 99]


# def test_modes_part_2():
# assert opcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]) == [1002, 4, 3, 4, 99]
# assert opcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]) == [1101, 100, -1, 4, 99]
# assert opcode([3, 3, 1108, -1, 8, 3, 4, 3, 99]) == [1, 0, 4, 0, 99]
# assert opcode([3, 3, 1107, -1, 8, 3, 4, 3, 99]) == [1, 0, 4, 0, 99]
