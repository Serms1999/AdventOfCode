from IO.IO_module import read_input_lines
import statistics


def get_paren_type(char: str) -> str:
    for paren_type in ['()', '[]', '{}', '<>']:
        if char in paren_type:
            return paren_type

    return ''


def get_complementary_paren(char: str) -> str:
    paren_type = get_paren_type(char)
    return list(set(paren_type) - set(char))[0]


def part1(input_lines: list) -> int:
    ponderation = {
        '()': 3,
        '[]': 57,
        '{}': 1197,
        '<>': 25137
    }
    open_list = []
    close_list = []
    for pattern in ponderation:
        a, b = pattern
        open_list += [a]
        close_list += [b]

    total_syntax_error_score = 0
    for line in input_lines:
        stack = []
        for char in line:
            if char in open_list:
                stack += [char]
            elif len(stack) > 0 and get_paren_type(stack[len(stack) - 1]) == get_paren_type(char):
                stack.pop()
            else:
                total_syntax_error_score += ponderation[get_paren_type(char)]
                break

    return total_syntax_error_score


def part2(input_lines: list) -> int:
    ponderation = {
        '()': 1,
        '[]': 2,
        '{}': 3,
        '<>': 4
    }
    open_list = []
    close_list = []
    for pattern in ponderation:
        a, b = pattern
        open_list += [a]
        close_list += [b]

    total_syntax_error_score = []
    for line in input_lines:
        stack = []
        corrupted = False
        for char in line:
            if char in open_list:
                stack += [char]
            elif len(stack) > 0 and get_paren_type(stack[len(stack) - 1]) == get_paren_type(char):
                stack.pop()
            else:
                corrupted = True
                break

        if not corrupted and len(stack) != 0:
            score = 0
            remaining_characters = list(reversed(stack))
            for char in remaining_characters:
                score = score * 5 + ponderation[get_paren_type(char)]
            total_syntax_error_score += [score]

    return statistics.median(total_syntax_error_score)


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
