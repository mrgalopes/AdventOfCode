from day7 import *

def test_parse_inner_bags():
    assert parse_inner_bags('no other bags.') == {}
    assert parse_inner_bags('3 bright white bags, 4 muted yellow bags.') == \
        {'bright white': 3, 'muted yellow': 4}
    assert parse_inner_bags('1 bright white bag, 2 muted yellow bags.') == \
        {'bright white': 1, 'muted yellow': 2}

parsed_example = {
    'light red': {'bright white': 1, 'muted yellow': 2},
    'dark orange': {'bright white': 3, 'muted yellow': 4},
    'bright white': {'shiny gold': 1},
    'muted yellow': {'shiny gold': 2, 'faded blue': 9},
    'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
    'dark olive': {'faded blue': 3, 'dotted black': 4},
    'vibrant plum': {'faded blue': 5, 'dotted black': 6},
    'faded blue': {},
    'dotted black': {},
}

def test_parse_bags_from_line():
    assert parse_bags('light red bags contain 1 bright white bag, 2 muted yellow bags.') == \
        {'light red': {'bright white': 1, 'muted yellow': 2}}

    example_given = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
    """
    assert parse_bags(example_given) == parsed_example

def test_count_outmost():
    assert count_outermost_with_certain_color(parsed_example, 'shiny gold') == \
        ['bright white', 'muted yellow']
    assert count_outermost_with_certain_color(parsed_example, 'bright white') == \
        ['light red', 'dark orange']
    assert count_outermost_with_certain_color(parsed_example, 'muted yellow') == \
        ['light red', 'dark orange']

def test_bag_total_count():
    assert count_bags_eventually_containing(parsed_example, 'shiny gold') == 4


example_part_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

def test_count_inner_bags():
    bags = parse_bags(example_part_2)
    assert count_inner_bags_with_color(bags, 'shiny gold') == 126
    assert count_inner_bags_with_color(parsed_example, 'shiny gold') == 32
