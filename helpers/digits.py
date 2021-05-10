from dataclasses import dataclass, field
from numpy import prod


def convert_digit(digit, index):
    if len(str(digit)) > 5:
        return Code404(value=digit, index=index)
    opcode = int(str(digit)[-2:])
    try:
        return globals()[f"Code{opcode}"](value=digit, index=index)
    except KeyError:
        return Code404(value=digit, index=index)


class HaltProgramException(Exception):
    """Stops the program."""

    pass


@dataclass(frozen=True)
class Digit:
    value: str = field(repr=False)
    index: int = field(repr=False)
    next_pointer: int = index + 4

    @property
    def op_code(self) -> int:
        return int(str(self.value)[-2:])

    @property
    def first_mode(self) -> int:
        return self._get_mode(degree=1)

    @property
    def second_mode(self) -> int:
        return self._get_mode(degree=2)

    @property
    def third_mode(self) -> int:
        return self._get_mode(degree=3)

    def _get_mode(self, degree: int) -> int:
        try:
            return int(str(self.value)[-2 - degree])
        except IndexError:
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
            new_item=sum([input_1_pos.value, input_2_pos.value]),
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
            new_item=prod([input_1_pos.value, input_2_pos.value]),
        )


class Code3(Digit):
    """[summary]"""

    self._next_pointer: int = 2

    def digit_function(
        self,
        memory_list,
    ):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        digit_input = int(input("User Input -> "))
        memory_list.replace_item(
            old_item=input_1_pos,
            new_item=digit_input,
        )


class Code4(Digit):
    """[summary]"""

    self._next_pointer: int = 2

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        print(f"Output value is: {input_1_pos.value}")


class Code5(Digit):
    """[summary]"""

    self._next_pointer: int = 3

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        if input_1_pos != 0:
            self.self._next_pointer = memory_list.find_position(
                index=self.index + 2, mode=self.second_mode
            ).value


class Code6(Digit):
    """[summary]"""

    self._next_pointer: int = 3

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        if input_1_pos == 0:
            self.self._next_pointer = memory_list.find_position(
                index=self.index + 2, mode=self.second_mode
            ).value


class Code7(Digit):
    """[summary]"""

    self._next_pointer: int = 4

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        input_2_pos = memory_list.find_position(
            index=self.index + 2, mode=self.second_mode
        )
        output_pos = memory_list.find_position(
            index=self.index + 3, mode=self.third_mode
        )
        if input_1_pos < input_2_pos:
            new_value = 1
        else:
            new_value = 0

        memory_list.replace_item(old_item=output_pos, new_item=new_value)


class Code8(Digit):
    """[summary]"""

    self._next_pointer: int = 4

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        input_2_pos = memory_list.find_position(
            index=self.index + 2, mode=self.second_mode
        )
        output_pos = memory_list.find_position(
            index=self.index + 3, mode=self.third_mode
        )
        if input_1_pos == input_2_pos:
            new_value = 1
        else:
            new_value = 0

        memory_list.replace_item(old_item=output_pos, new_item=new_value)


class Code99(Digit):
    """Program End Digit"""

    @property
    def next_pointer(self):
        return 1

    def digit_function(self, memory_list=None):
        raise HaltProgramException()


class Code404(Digit):
    """None functioning digits."""

    @property
    def next_pointer(self):
        return 1

    def digit_function(self, memory_list=None):
        pass
