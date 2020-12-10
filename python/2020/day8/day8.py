#!/usr/bin/env python3

def parse_instructions(input_list):
    return [instruction.split(' ') for instruction in input_list]

def execute(instruction_list):
    program_count = 0
    accumulator = 0
    instructions_executed = set()
    while True:
        if program_count in instructions_executed:
            return accumulator
        instructions_executed.add(program_count)
        program_count, accumulator = execute_instruction(instruction_list[program_count],
                                                         program_count,
                                                         accumulator)

def execute_instruction(instruction, program_count, accumulator):
    operator, operand = instruction
    if operator == 'nop':
        return program_count+1, accumulator
    if operator == 'acc':
        return program_count+1, accumulator+int(operand)
    if operator == 'jmp':
        return program_count+int(operand), accumulator

def nop_and_jmp_instruction_indices(instruction_list):
    return [i for i,[instruction, _] in enumerate(instruction_list)
            if instruction in ['nop', 'jmp']]

def execute_part_2(instruction_list):
    program_count = 0
    max_program_count = len(instruction_list)
    accumulator = 0
    instructions_executed = set()
    while True:
        if program_count in instructions_executed:
            return accumulator, False
        if program_count >= max_program_count:
            return accumulator, True
        instructions_executed.add(program_count)
        program_count, accumulator = execute_instruction(instruction_list[program_count],
                                                         program_count,
                                                         accumulator)

def accumulator_after_fixing_program(instruction_list):
    indices = nop_and_jmp_instruction_indices(instruction_list)
    for i in indices:
        previous_instruction = instruction_list[i][0]
        instruction_list[i][0] = 'nop' if previous_instruction == 'jmp' else 'jmp'
        accumulator, ended = execute_part_2(instruction_list)
        if ended:
            return accumulator
        instruction_list[i][0] = previous_instruction


def part1():
    with open('./input.txt') as f:
        input_str = f.read().strip().split('\n')
    instruction_list = parse_instructions(input_str)
    print(execute(instruction_list))

def part2():
    with open('./input.txt') as f:
        input_str = f.read().strip().split('\n')
    instruction_list = parse_instructions(input_str)
    print(accumulator_after_fixing_program(instruction_list))

if __name__ == '__main__':
    part2()
