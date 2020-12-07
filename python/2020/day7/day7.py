import re

def count_bags_eventually_containing(bags, color):
    outermost_bags = count_outermost_with_certain_color(bags, color)
    colors = set()
    i = 0
    while i < len(outermost_bags):
        outermost_color = outermost_bags[i]
        if outermost_color not in colors:
            new_outermost_bags = count_outermost_with_certain_color(bags, outermost_color)
            outermost_bags = outermost_bags + new_outermost_bags
            colors.add(outermost_color)
        i += 1
    return len(colors)


def count_outermost_with_certain_color(bags, color):
    outermost_bags = []
    for outermost_bag, inner_bags in bags.items():
        if color in inner_bags:
            outermost_bags.append(outermost_bag)
    return outermost_bags

def parse_bags(input_str):
    bags = {}
    for line in input_str.strip().split('\n'):
        outermost, inner_bags = line.split(' bags contain ')
        parsed_inner = parse_inner_bags(inner_bags)
        bags[outermost] = parsed_inner
    return bags

def parse_inner_bags(inner_bags_str):
    if inner_bags_str == 'no other bags.':
        return {}
    inner_bags = {}
    regex = re.compile(r'(\d+) (.+) bags?\.?')
    for bag_str in inner_bags_str.split(', '):
        match = regex.match(bag_str)
        num_bags = match.group(1)
        bag_color = match.group(2)
        inner_bags[bag_color] = int(num_bags)
    return inner_bags

def count_inner_bags_with_color(bags, color):
    if bags[color] == {}:
        return 0
    count = 0
    for bag_color, bag_count in bags[color].items():
        count += bag_count * count_inner_bags_with_color(bags, bag_color) + bag_count
    return count


def part1():
    with open('./input.txt') as f:
        bags = parse_bags(f.read())
    print(count_bags_eventually_containing(bags, 'shiny gold'))

def part2():
    with open('./input.txt') as f:
        bags = parse_bags(f.read())
    print(count_inner_bags_with_color(bags, 'shiny gold'))

if __name__ == '__main__':
    part2()
