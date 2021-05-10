from itertools import product

from helpers import OpcodeComputer
from helpers import AmplificationCircuit

data = [
    3,
    8,
    1001,
    8,
    10,
    8,
    105,
    1,
    0,
    0,
    21,
    46,
    59,
    80,
    105,
    122,
    203,
    284,
    365,
    446,
    99999,
    3,
    9,
    102,
    3,
    9,
    9,
    1001,
    9,
    5,
    9,
    102,
    2,
    9,
    9,
    1001,
    9,
    3,
    9,
    102,
    4,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    1002,
    9,
    2,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    101,
    5,
    9,
    9,
    1002,
    9,
    3,
    9,
    1001,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    99,
    3,
    9,
    1002,
    9,
    4,
    9,
    1001,
    9,
    2,
    9,
    102,
    4,
    9,
    9,
    101,
    3,
    9,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    102,
    5,
    9,
    9,
    101,
    4,
    9,
    9,
    102,
    3,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    99,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    99,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    99,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    101,
    2,
    9,
    9,
    4,
    9,
    99,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    101,
    1,
    9,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1002,
    9,
    2,
    9,
    4,
    9,
    3,
    9,
    1001,
    9,
    1,
    9,
    4,
    9,
    3,
    9,
    102,
    2,
    9,
    9,
    4,
    9,
    99,
]

amplification_circuit = AmplificationCircuit(number_of_amplifiers=5)

best_solution = [0, None]

for permutation in permutations(range(5), 5):
    result = amplification_circuit.run(circuit_input=0, phase_squence=permutation)
    if result > best_solution[0]:
        best_solution = [result, permutation]

print(f"Day 7 Part 1 answer is  [Highest Result, Sequence]->{best_solution}")