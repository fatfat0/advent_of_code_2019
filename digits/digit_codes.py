from helpers.digit_reader import convert_digit

from dataclasses import dataclass, field
import numpy as np


class HaltProgram:
    """Stops the program."""

    raise StopIteration


@dataclass(frozen=True)
class Digit:
    value: int = field(repr=False)
    index: int = field(repr=False)

    def digit_function(self, memory_list=None, parameter_mode=0):
        raise NotImplementedError

    def _read_by_index(self, position, memory_list):
        return next(item for item in memory_list if item.index == position)

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
        return HaltProgram()


class Code1(Digit):
    def digit_function(self, memory_list, parameter_mode=0):
        """input_1_pos and input_2_pos read position dats, output_pos store positon data"""
        input_1_pos, input_2_pos, output_pos = self._find_position(
            parameter_mode=parameter_mode
        )
        self._store_in_position(
            position=output_pos,
            value=sum(
                self._read_by_index(
                    position=input_1_pos, memory_list=memory_list
                ).value,
                self._read_by_index(
                    position=input_2_pos, memory_list=memory_list
                ).value,
            ),
        )


class Code2(Digit):
    def digit_function(self, memory_list, parameter_mode=0):
        """input_1_pos and input_2_pos read position dats, output_pos store positon data"""
        input_1_pos, input_2_pos, output_pos = self._find_position(
            parameter_mode=parameter_mode
        )
        self._store_in_position(
            position=output_pos,
            value=np.prod(
                self._read_by_index(
                    position=input_1_pos, memory_list=memory_list
                ).value,
                self._read_by_index(
                    position=input_2_pos, memory_list=memory_list
                ).value,
            ),
        )
