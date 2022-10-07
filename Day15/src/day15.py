from IO.IO_module import read_input_lines
import numpy as np


def part1(input_lines: list) -> int:
    cavern = np.array([list(row) for row in input_lines], dtype=int)

    return 0


def part2(input_lines: list) -> int:
    return 0


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
