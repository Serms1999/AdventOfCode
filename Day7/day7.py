import IO.IO_module as IO
import numpy as np


def part1(input_str: str) -> int:
    positions = np.array(input_str.split(','), dtype=int)
    sum_list = []
    for a in range(max(positions) + 1):
        partial_sum = 0
        for i, value in enumerate(positions):
            partial_sum += abs(positions[i] - a)
        sum_list += [partial_sum]

    return min(sum_list)


def part2(input_str: str) -> int:
    positions = np.array(input_str.split(','), dtype=int)
    sum_list = []
    for a in range(max(positions) + 1):
        partial_sum = 0
        for i, value in enumerate(positions):
            diff = abs(positions[i] - a)
            partial_sum += (diff * (diff + 1)) // 2
        sum_list += [partial_sum]

    return min(sum_list)


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines[0])}')
    print(f'Part two solution: {part2(input_lines[0])}')


if __name__ == '__main__':
    main()
