from helpers import amplifiers
from helpers.amplifiers import AmplificationCircuit, Amplifier

from pytest import fixture
from itertools import permutations


@fixture
def data():
    return [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]


def test_amplifier_circuit(data):
    amplification_circuit = AmplificationCircuit(program=data)

    result = amplification_circuit.run(
        phase_squence=[0, 1, 2, 3, 4],
        first_input=0,
        number_of_feedback=0,
    )
    assert result == 1234
    result = amplification_circuit.run(
        phase_squence=[0, 1, 2, 3, 4],
        first_input=0,
        number_of_feedback=1,
    )
    result == 123401234


def test_amplifier(data):
    amplifier = Amplifier(data)
    assert data == amplifier.program
    amplifier.run([4, 5])
    assert data != amplifier.program
    output_1 = amplifier.amplifier_output
    amplifier.run([4, 5])
    output_2 = amplifier.amplifier_output
    assert output_1 != output_2
