from IO.IO_module import read_input_lines
import os
import numpy as np


def read_input() -> list:
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, 'input')
    return read_input_lines(file_path)


def part1(measurements: np.ndarray) -> int:
    increments = measurements[1:] - measurements[:-1]
    return len(list(filter(lambda x: (x > 0), increments)))


def part2(measurements: np.ndarray):
    def slice_window(a, k):
        array = np.array(a)
        return [array[i:i + k] for i in range(len(array) - k + 1)]

    sums = np.array([sum(x) for x in slice_window(measurements, 3)])
    return part1(sums)


def main():
    input_lines = read_input_lines(root_file=__file__)
    measurements = np.array([int(n) for n in input_lines])
    print(f'Part one solution: {part1(measurements)}')
    print(f'Part two solution: {part2(measurements)}')


if __name__ == '__main__':
    main()
