
def is_valid_password(minimum, maximum, letter, password):
    count = 0
    for l in password:
        if l == letter:
            count += 1
    return count >= minimum and count <= maximum

def is_valid_password_2(pos1, pos2, letter, password):
    index1 = pos1 - 1
    index2 = pos2 - 1
    return password[index1] == letter and password[index2] != letter or \
           password[index1] != letter and password[index2] == letter

def part1():
    with open('./input.txt') as f:
        passwords = f.readlines()

    count = 0
    for line in passwords:
        interval, letter_with_colon, password = line.split(' ')
        minimum, maximum = [int(x) for x in interval.split('-')]
        letter = letter_with_colon[0:-1]
        if is_valid_password(minimum, maximum, letter, password):
            count += 1
    print(count)

def part2():
    with open('./input.txt') as f:
        passwords = f.readlines()

    count = 0
    for line in passwords:
        interval, letter_with_colon, password = line.split(' ')
        pos1, pos2 = [int(x) for x in interval.split('-')]
        letter = letter_with_colon[0:-1]
        if is_valid_password_2(pos1, pos2, letter, password):
            count += 1
    print(count)

if __name__ == '__main__':
    part2()
