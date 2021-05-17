from fixture import opcode, opcode_output


def test_modes_part_1():
    assert opcode(program_data=[1002, 4, 3, 4, 33], computer_inputs=[1]) == [
        1002,
        4,
        3,
        4,
        99,
    ]
    assert opcode(program_data=[1101, 100, -1, 4, 0], computer_inputs=[1]) == [
        1101,
        100,
        -1,
        4,
        99,
    ]


def test_day_5_part_2():
    assert (
        opcode_output(
            program_data=[
                3,
                21,
                1008,
                21,
                8,
                20,
                1005,
                20,
                22,
                107,
                8,
                21,
                20,
                1006,
                20,
                31,
                1106,
                0,
                36,
                98,
                0,
                0,
                1002,
                21,
                125,
                20,
                4,
                20,
                1105,
                1,
                46,
                104,
                999,
                1105,
                1,
                46,
                1101,
                1000,
                1,
                20,
                4,
                20,
                1105,
                1,
                46,
                98,
                99,
            ],
            computer_inputs=[7],
        )
        == 1000
    )
