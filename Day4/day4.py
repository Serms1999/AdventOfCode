import IO.IO_module as IO
import numpy as np


def parse_bingos(lines: list) -> list:
    bingos = []
    for i in range(len(lines) // 6):
        bingo = []
        for r in range(1, 6):
            bingo += [[int(n) for n in lines[6 * i + r].split()]]
        bingos += [bingo]

    return [np.array(b) for b in bingos]


def check_bingo_row(bingo: np.ndarray, numbers: set) -> bool:
    for r in bingo:
        if set(r).issubset(numbers):
            return True

    return False


def part1(lines: list) -> int:
    numbers = [int(n) for n in lines[0].split(',')]
    bingos = parse_bingos(lines[1:])

    for i in range(5, len(lines)):
        subset_numbers = set(numbers[0: i])
        for bingo in bingos:
            row = check_bingo_row(bingo, subset_numbers)
            if row:
                num = numbers[i - 1]
                diff = set(bingo.flatten()) - subset_numbers
                row_sum = sum(diff)
                return num * row_sum
            column = check_bingo_row(np.transpose(bingo), subset_numbers)
            if column:
                num = numbers[i - 1]
                diff = set(bingo.flatten()) - subset_numbers
                column_sum = sum(diff)
                return num * column_sum
    return 0


def part2(lines: list) -> int:
    numbers = [int(n) for n in lines[0].split(',')]
    bingos = parse_bingos(lines[1:])

    def remove_array(array_list, arr):
        ind = 0
        size = len(array_list)
        while ind != size and not np.array_equal(array_list[ind], arr):
            ind += 1
        if ind != size:
            array_list.pop(ind)
        else:
            raise ValueError('Array not found in list')

    for i in range(5, len(lines)):
        subset_numbers = set(numbers[0: i])
        for bingo in bingos:
            if len(bingos) == 1:
                num = numbers[i - 1]
                diff = set(bingos[0].flatten()) - subset_numbers
                unmarked_sum = sum(diff)
                return num * unmarked_sum

            row = check_bingo_row(bingo, subset_numbers)
            if row:
                remove_array(bingos, bingo)
            else:
                column = check_bingo_row(np.transpose(bingo), subset_numbers)
                if column:
                    remove_array(bingos, bingo)
    return 0


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
