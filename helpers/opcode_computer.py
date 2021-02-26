class OpcodeComputer:
    """Class representing our Integer Computer"""

    def __init__(self, program):
        """Initialize with program, given as a list of integers"""
        self.memory = program
        self.instruction_pointer = 0

    def set_inputs(self, inputs, addresses=[1, 2]):
        """Provide inputs in the form of a (noun, verb) tuple.

        Inputs are written into memory positions specified by the addresses (default 1
        and 2)
        """
        for input, address in zip(inputs, addresses):
            self.memory[address] = input

    def run(self):
        """Execute the program currently in the memory, until a 99 opcode is encountered.

        Note: As time goes on and more instructiosn get added, we would probably
        refactor this. Create a class for the various instructions and have them be
        responsible for computing the correct results.

        The "switch" statement for the opcodes would be put into a factory class /
        factory method that creates instruction objects."""
        while True:
            # Note: Right now we don't have to worry about endless loops, because the
            # current program doesn't jump around.
            if self.memory[self.instruction_pointer] == 99:
                return

            opcode, orig1, orig2, dest = self.memory[
                self.instruction_pointer : self.instruction_pointer + 4
            ]
            op1, op2 = self.memory[orig1], self.memory[orig2]

            if opcode == 1:
                self.memory[dest] = op1 + op2
            elif opcode == 2:
                self.memory[dest] = op1 * op2
            else:
                raise ValueError("Don't know this opcode")

            self.instruction_pointer += 4

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self.memory[address]

    def __getitem__(self, key):
        return self.memory[key]
