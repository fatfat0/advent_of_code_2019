from .memory_class import MemoryList
from .digits import HaltProgramException, PauseProgramException


class OpcodeComputer:
    """Class representing our Integer Computer"""

    def __init__(
        self,
        instruction_length=4,
        pointer_start_value: int = 0,
    ):
        """Initialize with program, given as a list of integers"""
        self._instruction_length = instruction_length
        self._index_pointer = pointer_start_value
        self.halted = False

    def run(
        self,
        program: list,
        computer_inputs: list = [],
        pausable: bool = False,
    ):
        """Execute the program currently in the memory, until a 99 opcode is encountered.

        Note: As time goes on and more instructiosn get added, we would probably
        refactor this. Create a class for the various instructions and have them be
        responsible for computing the correct results."""
        self._instructions = MemoryList(program)
        while True:
            try:
                self._instructions.memory[self._index_pointer].digit_function(
                    memory_list=self._instructions
                )
                self.set_pointer()
            except TypeError:
                computer_input = computer_inputs.pop(0)
                self._instructions.memory[self._index_pointer].digit_function(
                    memory_list=self._instructions, digit_input=computer_input
                )
                self.set_pointer()
            except PauseProgramException:
                self.set_pointer()
                if pausable:
                    break
                pass
            except HaltProgramException:
                self.halted = True
                break

    def set_pointer(self):
        self._index_pointer = self._instructions.memory[
            self._index_pointer
        ].next_pointer

    def get_results(self):
        return self._instructions.get_memory_codes()

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self._instructions.memory[address].value

    @property
    def diagnostic_output(self):
        return self._instructions.get_memory_output()

    @property
    def processed_program(self):
        return self._instructions.get_program()
