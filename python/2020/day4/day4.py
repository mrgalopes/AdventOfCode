
def has_required_fields(passport):
    expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in expected_fields:
        if field not in passport:
            return False
    return True


def has_validated_fields(passport):
    for field in passport.replace('\n', ' ').strip().split(' '):
        field_name, value = field.split(':')
        if field_name == 'byr':
            value = int(value)
            if value < 1920 or value > 2002:
                return False
        if field_name == 'iyr':
            value = int(value)
            if value < 2010 or value > 2020:
                return False
        if field_name == 'eyr':
            value = int(value)
            if value < 2020 or value > 2030:
                return False
        if field_name == 'hgt':
            unit = value[-2:]
            if unit != 'cm' and unit != 'in':
                return False
            value = int(value[:-2])
            if unit == 'cm' and (value < 150 or value > 193):
                return False
            if unit == 'in' and (value < 59 or value > 76):
                return False
        if field_name == 'hcl':
            if value[0] != '#':
                return False
            for c in value[1:]:
                if c not in '0123456789abcdef':
                    return False
        if field_name == 'ecl':
            valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value not in valid_eye_colors:
                return False
        if field_name == 'pid':
            if len(value) != 9:
                return False
            for num in value:
                if num not in '0123456789':
                    return False
    return True


def is_valid(passport):
    return has_required_fields(passport) and has_validated_fields(passport)


def main():
    with open('./input.txt') as f:
        valid_count = sum(is_valid(x) for x in f.read().split('\n\n'))
    print(valid_count)


if __name__=='__main__':
    main()
