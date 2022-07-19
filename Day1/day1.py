import IO.IO_module as IO
import numpy as np


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
    input_lines = IO.read_input_lines()
    measurements = np.array([int(n) for n in input_lines])
    print(f'Number of measurement increases: {part1(measurements)}')
    print(f'Number of sum increases: {part2(measurements)}')


if __name__ == '__main__':
    main()
