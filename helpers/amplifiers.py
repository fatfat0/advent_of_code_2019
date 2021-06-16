from helpers import OpcodeComputer


class Amplifier:
    def __init__(
        self,
        program: list,
    ) -> int:
        self.program = program
        self._computer = OpcodeComputer()

    def run(self, amplifier_inputs: list):
        self._computer.run(self.program, amplifier_inputs)
        self.program = self._computer.processed_program

    @property
    def amplifier_output(self):
        return self._computer.diagnostic_output


class AmplificationCircuit:
    def __init__(self, program: list, number_of_amplifiers: int = 5) -> None:
        self.program = program
        self._amplifiers = [
            Amplifier(program=program) for _ in range(number_of_amplifiers)
        ]

    def run(
        self, phase_squence: list, first_input: int = 0, number_of_feedback: int = 0
    ) -> int:
        amplifier_input = first_input
        feedback_count = 0
        while feedback_count <= number_of_feedback:
            for amplifier_squence, amplifier in zip(phase_squence, self._amplifiers):
                amplifier.run(
                    amplifier_inputs=[amplifier_squence, amplifier_input],
                )
                amplifier_input = amplifier.amplifier_output
            feedback_count += 1
        return amplifier_input
