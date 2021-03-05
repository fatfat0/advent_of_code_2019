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
        responsible for computing the correct results."""
        while True:
            # Note: Right now we don't have to worry about endless loops, because the
            # current program doesn't jump around.
            if self.memory[self.instruction_pointer] == 99:
                return

            opcode = self.memory[self.instruction_pointer]
            dest = self.memory[self.instruction_pointer + 3]

            opcode_method = self._get_opcode_method(opcode)
            self.memory[dest] = opcode_method()

            self.instruction_pointer += 4

    def _get_opcode_method(self, opcode):
        if opcode == 1:
            return self._opcode_sum
        if opcode == 2:
            return self._opcode_product
        else:
            raise ValueError(opcode)

    def _opcode_sum(self):
        op1, op2 = self._get_ops()
        return op1 + op2

    def _opcode_product(self):
        op1, op2 = self._get_ops()
        return op1 * op2

    def _get_ops(self):
        orig1, orig2 = self.memory[
            self.instruction_pointer + 1 : self.instruction_pointer + 3
        ]
        op1, op2 = self.memory[orig1], self.memory[orig2]
        return op1, op2

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self.memory[address]

    def __getitem__(self, key):
        return self.memory[key]
