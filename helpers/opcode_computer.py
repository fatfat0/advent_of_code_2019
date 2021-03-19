from helpers.digit_reader import convert_digits_to_class_list


class OpcodeComputer:
    """Class representing our Integer Computer"""

    def __init__(self, program):
        """Initialize with program, given as a list of integers"""
        # TODO can be init program in `run`, and `OpcodeComputer` init without data
        self.memory = convert_digits_to_class_list(program)

    def run(self):
        """Execute the program currently in the memory, until a 99 opcode is encountered.

        Note: As time goes on and more instructiosn get added, we would probably
        refactor this. Create a class for the various instructions and have them be
        responsible for computing the correct results."""
        # TODO find a way for pointer
        for index_pointer in range(len(self.memory)):
            self.memory[index_pointer].digit_function(memory_list=self.memory)

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self.memory[address]

    def __getitem__(self, key):
        return self.memory[key]
