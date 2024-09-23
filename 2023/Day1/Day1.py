from IO import read_input_lines


def get_num_or_empty_string(c: str) -> str:
    numbers = '0123456789'
    return c if c in numbers else ''


def map_spelled_numbers(s: str) -> str:
    s = s.replace('one', 'o1e')
    s = s.replace('two', 't2o')
    s = s.replace('three', 't3e')
    s = s.replace('four', 'f4r')
    s = s.replace('five', 'f5e')
    s = s.replace('six', 's6x')
    s = s.replace('seven', 's7n')
    s = s.replace('eight', 'e8t')
    s = s.replace('nine', 'n9e')
    return s.replace('zero', 'z0o')


def map_lines_into_numbers(s: str) -> int:
    first_digit = last_digit = None
    for c in [*s]:
        if str_num := get_num_or_empty_string(c):
            if first_digit is None:
                first_digit = str_num
            last_digit = str_num

    return int(f'{first_digit}{last_digit}')


def get_calibration_sum(lines: list[str]) -> int:
    return sum([map_lines_into_numbers(map_spelled_numbers(line)) for line in lines])


def main():
    input_lines = read_input_lines(file_name='input')
    print(f'Sum of the calibration numbers: {get_calibration_sum(input_lines)}')


if __name__ == '__main__':
    main()
