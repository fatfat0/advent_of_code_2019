class Amplifier:
    def __init__(self, program, amplifier_input: int, amplifier_squence: int) -> int:
        self.program = program
        self.amplifier_input = amplifier_num
        self.amplifier_squence = amplifier_squence
        self._computer = OpcodeComputer()
        self._computer.run(self.program, amplifier_input)
        return self._computer.output


class AmplificationCircuit:
    def __init__(
        self,
        program,
        phase_squence: iter[int],
    ) -> None:
        self.program = program
        self._phase_squence = phase_squence

    def run(
        self,
        phase_squence: iter[int],
    ) -> int:
        amplifier_input = 0
        for amplifier_squence in self._phase_squence:
            amplifier_input = Amplifier(
                program=self.program,
                amplifier_input=amplifier_input,
                amplifier_squence=amplifier_squence,
            )
        ### What is the difference between squence and input?
        return amplifier_input