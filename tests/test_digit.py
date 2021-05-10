from helpers.digits import convert_digit
from helpers.memory_class import MemoryList

from pytest import fixture


def test_convert_digit():
    test_digit = convert_digit(1002, 0)
    assert test_digit.value == 1002
    assert test_digit.index == 0
    assert test_digit.op_code == 2
    assert test_digit.first_mode == 0
    assert test_digit.second_mode == 1
    assert test_digit.third_mode == 0

    assert convert_digit(1, 0).op_code == convert_digit(99901, 0).op_code

    assert convert_digit("0011", 0).op_code == 11
    assert convert_digit("0011", 0).third_mode == 0


@fixture(scope="module")
def memory_list():
    return MemoryList([1, 0, 0, 3, 1, 1, 2, 3, 99])


def test_digit_class_1(memory_list):
    test_digit = convert_digit(11101, 0)

    assert memory_list.read_by_index(3).op_code == 3
    test_digit.digit_function(memory_list)
    assert memory_list.read_by_index(3).op_code == 1
