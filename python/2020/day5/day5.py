#!/usr/bin/env python3

def main():
    highest = 0
    seats = set()
    with open('./input.txt') as f:
        for line in f:
            seat_ID = parse_boarding_pass(line.strip())
            seats.add(seat_ID)
            if seat_ID > highest:
                highest = seat_ID
    print(highest)
    for i in range(highest):
        if i not in seats:
            print(i)



def parse_boarding_pass(boarding_pass):
    row = parse_row(boarding_pass[:7])
    column = parse_column(boarding_pass[7:])
    return parse_seat_ID(row=row, column=column)

def parse_row(region):
    row = 0
    for r in region:
        row = row << 1 # goes to next bit
        if r == 'B':
            row = row | 1 # sets last bit
    return row

def parse_column(region):
    col = 0
    for c in region:
        col = col << 1
        if c == 'R':
            col = col | 1
    return col

def parse_seat_ID(row, column):
    return row*8 + column

if __name__=='__main__':
    main()
