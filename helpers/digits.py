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


class PauseProgramException(Exception):
    """Pauses the program."""

    pass
    # def __init__(self, output_value):
    #     self.output = output_value


@dataclass(frozen=True)
class Digit:
    value: str = field(repr=False)
    index: int = field(repr=False)

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

    @property
    def next_pointer(self):
        return self.index + 4

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
    """takes a single integer as input and saves it to the position given by its only parameter.
    For example, the instruction 3,50 would take an input value and store it at address 50."""

    @property
    def next_pointer(self):
        return self.index + 2

    def digit_function(self, memory_list, digit_input: int):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        memory_list.replace_item(
            old_item=input_1_pos,
            new_item=digit_input,
        )


class Code4(Digit):
    """Opcode 4 outputs the value of its only parameter.
    For example, the instruction 4,50 would output the value at address 50."""

    @property
    def next_pointer(self):
        return self.index + 2

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        memory_list.memory_outputs.append(input_1_pos.value)
        raise PauseProgramException()


class Code5(Digit):
    """Opcode 5 is jump-if-true: if the first parameter is non-zero,
    it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""

    pointer_value: int = 3

    @property
    def next_pointer(self):
        return self.index + self.pointer_value

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        if input_1_pos.value != 0:
            self.pointer_value = (
                memory_list.find_position(
                    index=self.index + 2, mode=self.second_mode
                ).value
                - self.index
            )


class Code6(Digit):
    """Opcode 6 is jump-if-false: if the first parameter is zero,
    it sets the instruction pointer to the value from the second parameter.
    Otherwise, it does nothing."""

    pointer_value: int = 3

    @property
    def next_pointer(self):
        return self.index + self.pointer_value

    def digit_function(self, memory_list):
        input_1_pos = memory_list.find_position(
            index=self.index + 1, mode=self.first_mode
        )
        if input_1_pos.value == 0:
            self.pointer_value = (
                memory_list.find_position(
                    index=self.index + 2, mode=self.second_mode
                ).value
                - self.index
            )


class Code7(Digit):
    """Opcode 7 is less than: if the first parameter is less than the second parameter,
    it stores 1 in the position given by the third parameter.
    Otherwise, it stores 0."""

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
        if input_1_pos.value < input_2_pos.value:
            new_value = 1
        else:
            new_value = 0

        memory_list.replace_item(old_item=output_pos, new_item=new_value)


class Code8(Digit):
    """Opcode 8 is equals: if the first parameter is equal to the second parameter,
    it stores 1 in the position given by the third parameter.
    Otherwise, it stores 0."""

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
        if input_1_pos.value == input_2_pos.value:
            new_value = 1
        else:
            new_value = 0

        memory_list.replace_item(old_item=output_pos, new_item=new_value)


class Code99(Digit):
    """Program End Digit"""

    @property
    def next_pointer(self):
        return self.index + 1

    def digit_function(self, memory_list=None):
        raise HaltProgramException()


class Code404(Digit):
    """None functioning digits."""

    @property
    def next_pointer(self):
        return self.index + 1

    def digit_function(self, memory_list=None):
        pass
