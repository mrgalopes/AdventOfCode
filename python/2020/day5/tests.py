#!/usr/bin/env python3
from day5 import parse_row, parse_column, parse_seat_ID, parse_boarding_pass

def test_parse_row():
    assert parse_row('BFFFBBF') == 70
    assert parse_row('FFFBBBF') == 14
    assert parse_row('BBFFBBF') == 102

def test_parse_col():
    assert parse_column('RRR') == 7
    assert parse_column('RLL') == 4
    assert parse_column('RLR') == 5

def test_parse_seat_ID():
    assert parse_seat_ID(row=70, column=7) == 567
    assert parse_seat_ID(row=14, column=7) == 119
    assert parse_seat_ID(row=102, column=4) == 820

def test_parse_boarding_pass():
    assert parse_boarding_pass('BFFFBBFRRR') == 567
    assert parse_boarding_pass('FFFBBBFRRR') == 119
    assert parse_boarding_pass('BBFFBBFRLL') == 820
