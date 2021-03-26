from math import prod


def Code1(memory, instruction_pointer, parameter_modes):
    """Class representing our Code1 (sum)"""
    parameters = get_parameters(memory, instruction_pointer, 3)
    dest = parameters[2]
    inputs = get_inputs(memory, parameters[:2], parameter_modes[:2])
    memory[dest] = sum(inputs)

    return memory


def Code2(memory, instruction_pointer, parameter_modes):
    """Class representing our Code2 (product)"""
    parameters = get_parameters(memory, instruction_pointer, 3)
    dest = parameters[2]
    inputs = get_inputs(memory, parameters[:2], parameter_modes[:2])
    memory[dest] = prod(inputs)
    return memory


def Code3(memory, instruction_pointer, parameter_modes):
    """Class representing our Code3 (input)"""
    parameters = get_parameters(memory, instruction_pointer, 1)
    dest = parameters[0]
    memory[dest] = int(input("Please enter input value (int)"))
    return memory


def Code4(memory, instruction_pointer, parameter_modes):
    """Class representing our Code4 (output)"""
    parameters = get_parameters(memory, instruction_pointer, 1)
    dest = parameters[0]
    output_val = get_inputs(memory, parameters, parameter_modes)[0]
    # output_val = memory[dest]
    print(f"Output value {output_val}")
    return memory


def Code404(memory, instruction_pointer):
    """Class representing our Code2 (product)"""
    raise NotImplementedError


def get_inputs(memory, parameters, parameter_modes):
    inputs = []
    for param, mode in zip(parameters, parameter_modes):
        if mode == 0:
            inputs.append(memory[param])
        elif mode == 1:
            inputs.append(param)
    return inputs


def get_parameters(memory, init_pointer, length):
    return [memory[x] for x in range(init_pointer + 1, init_pointer + 1 + length)]


def get_opcode_method(opcode):
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


def get_opcode_length(opcode):
    if opcode in [1, 2]:
        return 3
    elif opcode in [3, 4]:
        return 1
    else:
        return ValueError(f"Opcode {opcode} is not supported")


def get_opcode_and_parameter_modes(instruction):
    opcode = int(str(instruction)[-2:])  # the two right-most digits are the opcode
    opcode_length = get_opcode_length(opcode)
    opcode_mode_str = str(instruction)[:-2].zfill(
        opcode_length
    )  # up to 3 digits after opcode
    # the first param mode corresponds to the hundreds unit, second to thousands,
    # etc, so first reverse the left parth of the instruction corresponding to the
    # instruction set, then convert it back to ints.
    parameter_modes = list(map(int, list(opcode_mode_str)[::-1]))
    return opcode, parameter_modes


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

            # from IPython import embed

            # embed()
            instruction = self.memory[self.instruction_pointer]
            opcode, parameter_modes = get_opcode_and_parameter_modes(instruction)
            opcode_method = get_opcode_method(opcode)
            self.memory = opcode_method(
                self.memory, self.instruction_pointer, parameter_modes
            )
            self.instruction_pointer += increase_pointer(opcode)

    @property
    def output(self, address=0):
        """The output of the program is considered to be whatever sits at position
        'address' in the memory (default 0)."""
        return self.memory[address]

    def __getitem__(self, key):
        return self.memory[key]
