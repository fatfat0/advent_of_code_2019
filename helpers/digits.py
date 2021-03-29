from dataclasses import dataclass, field
from numpy import prod


class HaltProgramException(Exception):
    """Stops the program."""

    pass


@dataclass(frozen=True)
class Digit:
    value: str = field(repr=False)
    index: int = field(repr=False)

    @property
    def op_code(self):
        return int(str(self.value)[-2:])

    @property
    def first_mode(self):
        return self._get_mode(degree=1)

    @property
    def second_mode(self):
        return self._get_mode(degree=2)

    @property
    def third_mode(self):
        return self._get_mode(degree=3)

    def _get_mode(self, degree):
        try:
            return int(str(self.value)[-2 - degree :: -1 - degree])
        except ValueError:
            return 0

    def digit_function(self, memory_list=None):
        raise NotImplementedError


# Function OPCodes Below ...


class Code1(Digit):
    def digit_function(self, memory_list):
        """input_1_pos and input_2_pos read position dats, output_pos store positon data"""
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        input_2_pos = memory_list.find_position(
            index=self.index + 2, mode=self.second_mode
        )
        output_pos = memory_list.find_position(
            index=self.index + 3, mode=self.third_mode
        )
        memory_list.replace_item(
            old_item=output_pos,
            new_item=sum([input_1_pos.op_code, input_2_pos.op_code]),
        )


class Code2(Digit):
    def digit_function(self, memory_list):
        """input_1_pos and input_2_pos read position dats, output_pos store positon data"""
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        input_2_pos = memory_list.find_position(
            index=self.index + 2, mode=self.second_mode
        )
        output_pos = memory_list.find_position(
            index=self.index + 3, mode=self.third_mode
        )
        memory_list.replace_item(
            old_item=output_pos,
            new_item=prod([input_1_pos.op_code, input_2_pos.op_code]),
        )


class Code3(Digit):
    """[summary]"""

    def digit_function(self, memory_list):
        raise NotImplementedError


class Code4(Digit):
    """[summary]"""

    def digit_function(self, memory_list):
        raise NotImplementedError


class Code99(Digit):
    """Program End Digit"""

    def digit_function(self, memory_list=None):
        return HaltProgramException()


class Code404(Digit):
    """None functioning digits."""

    def digit_function(self, memory_list=None):
        pass
