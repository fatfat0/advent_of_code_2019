from .digits import convert_digit


class MemoryList:
    """Class for storing and processing instructions list if digit classes"""

    def __init__(self, program_instructions):
        self.memory = self._convert_digits_to_class_list(program_instructions)
        self.memory_outputs = {0}

    def _convert_digits_to_class_list(self, data_list):
        return [convert_digit(digit, index) for index, digit in enumerate(data_list)]

    def get_memory_codes(self):
        return [digit.value for digit in self.memory]

    def read_by_index(self, position):
        return self.memory[self.memory[position].value]

    def replace_item(self, old_item, new_item):
        index = old_item.index
        self.memory.pop(index)
        self.memory.insert(index, convert_digit(digit=new_item, index=index))

    def find_position(self, index, mode=0):
        if mode == 0:
            return self.memory[self.memory[index].value]
        elif mode == 1:
            return self.memory[index]
        else:
            return ValueError(f"Opcode mode {mode} is not supported")

    def get_memory_output(self):
        return max(self.memory_outputs)
