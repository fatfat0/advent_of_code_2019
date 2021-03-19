def Code1(memory, instruction_pointer):
    """Class representing our Code2 (product)"""
    input_1_pos = memory[instruction_pointer + 1]
    input_2_pos = memory[instruction_pointer + 2]
    dest = memory[instruction_pointer + 3]
    memory[dest] = memory[input_1_pos] + memory[input_2_pos]
    return memory


def Code2(memory, instruction_pointer):
    """Class representing our Code2 (product)"""
    input_1_pos = memory[instruction_pointer + 1]
    input_2_pos = memory[instruction_pointer + 2]
    dest = memory[instruction_pointer + 3]
    memory[dest] = memory[input_1_pos] * memory[input_2_pos]
    return memory


def Code3(memory, instruction_pointer, input_val):
    """Class representing our Code2 (product)"""
    dest = memory[instruction_pointer + 1]
    memory[dest] = input_val
    return memory


def Code4(memory, instruction_pointer, output_val):
    """Class representing our Code2 (product)"""
    dest = memory[instruction_pointer + 1]
    output_val = memory[dest]
    return output_val


def Code404(memory, instruction_pointer):
    """Class representing our Code2 (product)"""
    raise NotImplementedError


def convert_digit(opcode):
    try:
        return globals()[f"Code{opcode}"]
    except:
        # TODO write down the error
        return Code404


def increase_pointer(opcode):
    """Define pointer increase based on opcode"""
    if opcode in [1, 2]:
        return 4
    elif opcode in [3, 4]:
        return 2
    else:
        return ValueError(f"Opcode {opcode} is not supported")


def get_opcode_parameter_modes(instruction):
    opcode = int(str(instruction)[-2:])  # the two right-most digits are the opcode
    param_mode_str = str(instruction).zfill(5)[:-2]  # up to 3 digits after opcode
    # the first param mode corresponds to the hundreds unit, second to thousands,
    # etc, so first reverse the left parth of the instruction corresponding to the
    # instruction set, then convert it back to ints.
    param_modes = list(map(int, list(param_mode_str)[::-1]))
    return opcode, param_modes


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

            instruction = self.memory[self.instruction_pointer]
            opcode, parameter_modes = get_opcode_parameter_modes(instruction)
            opcode_method = convert_digit(opcode)
            self.memory = opcode_method(self.memory, self.instruction_pointer)
            self.instruction_pointer += increase_pointer(opcode)

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self.memory[address]

    def __getitem__(self, key):
        return self.memory[key]
