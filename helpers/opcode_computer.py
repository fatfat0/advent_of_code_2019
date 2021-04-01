from .memory_class import MemoryList
from .digits import HaltProgramException


class OpcodeComputer:
    """Class representing our Integer Computer"""

    def __init__(self, instruction_length=4):
        """Initialize with program, given as a list of integers"""
        self._instruction_length = instruction_length

    def run(self, program:list):
        """Execute the program currently in the memory, until a 99 opcode is encountered.

        Note: As time goes on and more instructiosn get added, we would probably
        refactor this. Create a class for the various instructions and have them be
        responsible for computing the correct results."""
        self._instructions = MemoryList(program)
        try:
            for index_pointer in range(
                0, len(self._instructions.memory), self._instruction_length
            ):
                # TODO index pointer will require more advance function...
                self._instructions.memory[index_pointer].digit_function(
                    memory_list=self._instructions
                )
        except HaltProgramException:
            print("End Program.")

    def get_results(self):
        return self._instructions.get_memory_codes()

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self._instructions.memory[address].op_code
