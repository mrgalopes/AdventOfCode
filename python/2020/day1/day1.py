#!/usr/bin/env python3

def part1():
    with open('./input.txt') as f:
        stars = [int(x) for x in f.readlines()]

    for i in range(len(stars)):
        for j in range(i, len(stars)):
            first = stars[i]
            second = stars[j]
            if first + second == 2020:
                print(first)
                print(second)
                print(f'{first} + {second} = {first+second}')
                print(f'{first} * {second} = {first*second}')
                break


def part2():
    with open('./input.txt') as f:
        stars = [int(x) for x in f.readlines()]

    for i in range(len(stars)):
        first = stars[i]
        for j in range(i, len(stars)):
            second = stars[j]
            if first + second < 2020:
                for k in range(j, len(stars)):
                    third = stars[k]
                    if first + second + third == 2020:
                        print(first)
                        print(second)
                        print(third)
                        print(f'{first} + {second} + {third} = {first+second+third}')
                        print(f'{first} * {second} * {third} = {first*second*third}')
                        break


if __name__ == '__main__':
    part2()
