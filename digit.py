from dataclasses import dataclass, field
import numpy as np


class HaltProgram:
    """Stops the program."""

    raise NotImplementedError


@dataclass(frozen=True)
class Digit:
    value: int = field(repr=False)
    index: int = field(repr=False)

    def digit_function(self):
        raise NotImplementedError

    def _read_from_two_position(self, position_1, position_2):
        return NotImplementedError

    def _store_in_position(self, position, value):
        return NotImplementedError


class Code404(Digit):
    """None functioning digits."""

    def digit_function(self):
        pass


@dataclass(frozen=True)
class Code99(Digit):
    """Program finished...
    Args:
        Digit ([type]): [description]
    """

    def digit_function(self):
        return HaltProgram()


class Code1(Digit):
    def digit_function(self):
        """a and b read position dats, c store positon data"""
        input_1_pos = self.index + 1
        input_2_pos = self.index + 2
        output_pos = self.index + 3
        self._store_in_position(
            position=output_pos,
            value=sum(
                self._read_from_two_positions(
                    position_1=input_1_pos, position_2=input_2_pos
                )
            ),
        )


class Code2(Digit):
    def digit_function(self):
        """a and b read position dats, c store positon data"""
        input_1_pos = self.index + 1
        input_2_pos = self.index + 2
        output_pos = self.index + 3
        self._store_in_position(
            position=output_pos,
            value=np.prod(
                self._read_from_two_positions(
                    position_1=input_1_pos, position_2=input_2_pos
                )
            ),
        )