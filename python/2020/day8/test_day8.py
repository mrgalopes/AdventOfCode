from day8 import *

def test_instruction_execution():
    assert execute_instruction(['nop', '+3'], program_count=2, accumulator=2) ==  \
        (3, 2)
    assert execute_instruction(['acc', '+1'], program_count=5, accumulator=2) ==  \
        (6, 3)
    assert execute_instruction(['acc', '-105'], program_count=32, accumulator=300) ==  \
        (33, 195)
    assert execute_instruction(['jmp', '+3'], program_count=60, accumulator=15) ==  \
        (63, 15)
    assert execute_instruction(['jmp', '-5'], program_count=60, accumulator=15) ==  \
        (55, 15)

example_str = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_parse_instructions():
    input_list = example_str.strip().split('\n')
    assert parse_instructions(input_list) == [
        ['nop', '+0'],
        ['acc', '+1'],
        ['jmp', '+4'],
        ['acc', '+3'],
        ['jmp', '-3'],
        ['acc', '-99'],
        ['acc', '+1'],
        ['jmp', '-4'],
        ['acc', '+6'],
    ]

def test_part_1():
    input_list = example_str.strip().split('\n')
    instruction_list = parse_instructions(input_list)
    assert execute(instruction_list) == 5


def test_list_indices_of_nop_and_jmp():
    input_list = example_str.strip().split('\n')
    instruction_list = parse_instructions(input_list)
    assert nop_and_jmp_instruction_indices(instruction_list) == [0, 2, 4, 7]

def test_part_2():
    input_list = example_str.strip().split('\n')
    instruction_list = parse_instructions(input_list)
    assert accumulator_after_fixing_program(instruction_list) == 8
