from helpers import OpcodeComputer


class Amplifier:
    def __init__(
        self,
        program,
        amplifier_inputs: list,
    ) -> int:
        self.program = program
        self._computer = OpcodeComputer()
        self._computer.run(self.program, amplifier_inputs)

    @property
    def amplifier_output(self):
        return self._computer.diagnostic_output


class AmplificationCircuit:
    def __init__(
        self,
        program,
    ) -> None:
        self.program = program

    def run(self, phase_squence: list, first_input: int = 0) -> int:
        amplifier_input = first_input
        for amplifier_squence in phase_squence:
            amplifier = Amplifier(
                program=self.program,
                amplifier_inputs=[amplifier_squence, amplifier_input],
            )
            amplifier_input = amplifier.amplifier_output
        return amplifier_input
