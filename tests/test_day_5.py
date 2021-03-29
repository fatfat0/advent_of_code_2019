from fixture import opcode


def test_modes():
    assert opcode([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]
