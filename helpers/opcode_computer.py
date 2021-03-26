# from helpers.digit_reader import convert_digits_to_class_list

from dataclasses import dataclass, field
import numpy as np


class OpcodeComputer:
    """Class representing our Integer Computer"""

    def __init__(self, program, instruction_length=4):
        """Initialize with program, given as a list of integers"""
        # TODO can be init program in `run`, and `OpcodeComputer` init without data
        self.memory = convert_digits_to_class_list(program)
        self._instruction_length = instruction_length

    def run(self):
        """Execute the program currently in the memory, until a 99 opcode is encountered.

        Note: As time goes on and more instructiosn get added, we would probably
        refactor this. Create a class for the various instructions and have them be
        responsible for computing the correct results."""
        try:
            for index_pointer in range(0, len(self.memory), self._instruction_length):
                self.memory[index_pointer].digit_function(memory_list=self.memory)
        except HaltProgramException:
            print("End Program.")

    def get_results(self):
        return [digit.value for digit in self.memory]

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self.memory[address]

    def __getitem__(self, key):
        return self.memory[key]


class HaltProgramException(Exception):
    """Stops the program."""

    pass


@dataclass(frozen=True)
class Digit:
    value: int = field(repr=False)
    index: int = field(repr=False)

    def digit_function(self, memory_list=None, parameter_mode=0):
        raise NotImplementedError

    def _read_by_index(self, position, memory_list):
        return memory_list[memory_list[position].value]

    def _store_in_position(self, position=None, value=None, memory_list=None):
        del memory_list[position]
        memory_list.insert(position, convert_digit(digit=value, index=position))

    def _find_position(self, parameter_mode=0):
        if parameter_mode == 0:
            return self.index + 1, self.index + 2, self.index + 3
        elif parameter_mode == 1:
            return NotImplementedError
        else:
            return NotImplementedError


class Code404(Digit):
    """None functioning digits."""

    def digit_function(self, memory_list=None, parameter_mode=0):
        pass


@dataclass(frozen=True)
class Code99(Digit):
    """Program finished...
    Args:
        Digit ([type]): [description]
    """

    def digit_function(self, memory_list=None, parameter_mode=0):
        return HaltProgramException()


class Code1(Digit):
    def digit_function(self, memory_list, parameter_mode=0):
        """input_1_pos and input_2_pos read position dats, output_pos store positon data"""
        input_1_pos, input_2_pos, output_pos = self._find_position(
            parameter_mode=parameter_mode
        )
        self._store_in_position(
            position=self._read_by_index(
                position=output_pos, memory_list=memory_list
            ).index,
            value=sum(
                (
                    self._read_by_index(
                        position=input_1_pos, memory_list=memory_list
                    ).value,
                    self._read_by_index(
                        position=input_2_pos, memory_list=memory_list
                    ).value,
                )
            ),
            memory_list=memory_list,
        )


class Code2(Digit):
    def digit_function(self, memory_list, parameter_mode=0):
        """input_1_pos and input_2_pos read position dats, output_pos store positon data"""
        input_1_pos, input_2_pos, output_pos = self._find_position(
            parameter_mode=parameter_mode
        )
        self._store_in_position(
            position=self._read_by_index(
                position=output_pos, memory_list=memory_list
            ).index,
            value=np.prod(
                [
                    self._read_by_index(
                        position=input_1_pos, memory_list=memory_list
                    ).value,
                    self._read_by_index(
                        position=input_2_pos, memory_list=memory_list
                    ).value,
                ]
            ),
            memory_list=memory_list,
        )


def convert_digits_to_class_list(data_list):
    return [convert_digit(digit, index) for index, digit in enumerate(data_list)]


def convert_digit(digit, index):
    try:
        return globals()[f"Code{digit}"](digit, index)
    except KeyError:
        return Code404(digit, index)
