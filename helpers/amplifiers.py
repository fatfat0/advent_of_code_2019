from helpers.digits import HaltProgramException
from helpers import OpcodeComputer


class Amplifier:
    def __init__(
        self,
        program: list,
    ) -> int:
        self.program = program
        self._computer = OpcodeComputer()

    def run(self, amplifier_inputs: list):
        self._computer.run(self.program, amplifier_inputs, pausable=True)
        self.program = self._computer.processed_program
        if self._computer.halted:
            raise HaltProgramException()

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
        self, phase_squence: list, first_input: int = 0, feedback_loop: bool = False
    ) -> int:
        amplifier_input = first_input
        print(f"this is fist loop:{amplifier_input}")
        print(f"phase_squence:{phase_squence}")
        while True:
            try:
                for amplifier_squence, amplifier in zip(
                    phase_squence, self._amplifiers
                ):
                    print(f"amplifier_squence {amplifier_squence}")
                    amplifier.run(
                        amplifier_inputs=[amplifier_squence, amplifier_input],
                    )
                    amplifier_input = amplifier.amplifier_output
                if not feedback_loop:
                    print(f"amplifier_input_feedback:{amplifier_input}")
                    return amplifier_input
            except HaltProgramException:
                print(f"amplifier_input:{amplifier_input}")
                return amplifier_input
