#!/usr/bin/env python3

def count_questions_from_group(group):
    letters = set()
    for letter in group:
        if letter == '\n':
            continue
        letters.add(letter)
    return len(letters)

def count_agreed_questions_from_group(group_str):
    group_list = group_str.strip().split('\n')
    agreed_answers = set()
    first_group = True
    for group in group_list:
        if first_group:
            for letter in group:
                agreed_answers.add(letter)
            first_group = False
        else:
            next_person_answers = set()
            for letter in group:
                next_person_answers.add(letter)
            agreed_answers = agreed_answers.intersection(next_person_answers)
    return len(agreed_answers)


def part1():
    with open('./input.txt') as f:
        groups = f.read().split('\n\n')
    sum_counts = sum(count_questions_from_group(group) for group in groups)
    print(sum_counts)

def part2():
    with open('./input.txt') as f:
        groups = f.read().split('\n\n')
    sum_counts = sum(count_agreed_questions_from_group(group) for group in groups)
    print(sum_counts)


if __name__=='__main__':
    part2()
