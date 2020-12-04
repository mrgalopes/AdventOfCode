#!/usr/bin/env python3

def count_trees(trees, slope, down=1):
    tree_count = 0
    position = 0
    for i in range(0, len(trees), down):
        tree = trees[i]
        if position >= len(tree):
            position = position % len(tree)
        if tree[position] == '#':
            tree_count += 1
        position += slope

    return tree_count


def main():
    with open('./input.txt') as f:
        trees = [x.strip() for x in f.readlines()]

    slopes_mult = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for (slope, down) in slopes:
        slopes_mult *= count_trees(trees, slope, down=down)

    print(slopes_mult)



if __name__=='__main__':
    main()
