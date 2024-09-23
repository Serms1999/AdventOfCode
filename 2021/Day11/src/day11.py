from IO.IO_module import read_input_lines
import numpy as np


def add_tuples(t1: tuple, t2: tuple) -> tuple:
    return t1[0] + t2[0], t1[1] + t2[1]


def get_possibilities(position: tuple, arr_size: tuple) -> list:
    i, j = position
    num_rows, num_cols = arr_size
    possibilities = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    if i == 0:
        for p in range(-1, 2):
            possibilities.remove((-1, p))
    elif i == num_rows - 1:
        for p in range(-1, 2):
            possibilities.remove((1, p))

    if j == 0:
        for p in range(-1, 2):
            if (p, -1) in possibilities:
                possibilities.remove((p, -1))
    elif j == num_cols - 1:
        for p in range(-1, 2):
            if (p, 1) in possibilities:
                possibilities.remove((p, 1))

    return possibilities


def flash(arr: np.ndarray, position: tuple, flashed: np.ndarray) -> int:
    i, j = position
    num_flashes = 0

    if arr[i, j] < 9 or flashed[i, j]:
        arr[i, j] += 1
        return num_flashes

    possibilities = get_possibilities(position, np.shape(arr))
    flashed[i, j] = True
    for p in possibilities:
        x, y = add_tuples(position, p)
        if not flashed[x, y]:
            num_flashes += flash(arr, (x, y), flashed)

    return num_flashes + 1


def part1(input_lines: list) -> int:
    energy_levels = []
    for line in input_lines:
        energy_levels += [np.array([int(n) for n in line])]

    energy_levels = np.array(energy_levels)
    num_rows, num_cols = np.shape(energy_levels)
    flashed = np.zeros(num_rows * num_cols, dtype=bool).reshape((num_rows, num_cols))
    num_flashes = 0

    for _ in range(100):
        for i, row in enumerate(energy_levels):
            for j, octo in enumerate(row):
                num_flashes += flash(energy_levels, (i, j), flashed)

        for i, row in enumerate(flashed):
            for j, octo_flash in enumerate(row):
                if octo_flash:
                    energy_levels[i, j] = 0
                    flashed[i, j] = False

    return num_flashes


def part2(input_lines: list) -> int:
    energy_levels = []
    for line in input_lines:
        energy_levels += [np.array([int(n) for n in line])]

    energy_levels = np.array(energy_levels)
    num_rows, num_cols = np.shape(energy_levels)
    flashed = np.zeros(num_rows * num_cols, dtype=bool).reshape((num_rows, num_cols))
    step = 1

    while True:
        for i, row in enumerate(energy_levels):
            for j, octo in enumerate(row):
                flash(energy_levels, (i, j), flashed)

        for i, row in enumerate(flashed):
            for j, octo_flash in enumerate(row):
                if octo_flash:
                    energy_levels[i, j] = 0
                    flashed[i, j] = False

        if sum(sum(energy_levels)) == 0:
            break
        step += 1

    return step


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
