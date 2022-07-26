import IO.IO_module as IO
import numpy as np


def add_tuples(t1: tuple, t2: tuple) -> tuple:
    return t1[0] + t2[0], t1[1] + t2[1]


def get_possibilities(position: tuple, arr_size: tuple) -> list:
    i, j = position
    num_rows, num_cols = arr_size
    possibilities = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    if i == 0:
        possibilities.remove((-1, 0))
    elif i == num_rows - 1:
        possibilities.remove((1, 0))

    if j == 0:
        possibilities.remove((0, -1))
    elif j == num_cols - 1:
        possibilities.remove((0, 1))

    return possibilities


def get_adjacent_locations(arr: np.ndarray, position: tuple) -> list:
    i, j = position
    return [arr[i + x, j + y] for x, y in get_possibilities(position, np.shape(arr))]


def is_low_point(num: int, adjacent_location: list) -> bool:
    return num < min(adjacent_location)


def get_basin_size(arr: np.ndarray, position: tuple, visited: np.ndarray) -> int:
    i, j = position
    visited[i, j] = True

    size = 0
    if arr[i, j] == 9:
        return size

    possibilities = get_possibilities(position, np.shape(arr))
    for p in possibilities:
        x, y = add_tuples(position, p)
        if not visited[x, y]:
            size += get_basin_size(arr, (x, y), visited)

    return size + 1


def part1(lines: list) -> int:
    num_rows = len(lines)
    num_cols = len(lines[0])
    heightmap = np.reshape(np.array([int(x) for xs in lines for x in xs]), (num_rows, num_cols))
    low_points = []
    for i, row in enumerate(heightmap):
        for j, num in enumerate(row):
            if is_low_point(num, get_adjacent_locations(heightmap, (i, j))):
                low_points += [num + 1]

    return sum(low_points)


def part2(lines: list) -> int:
    num_rows = len(lines)
    num_cols = len(lines[0])
    heightmap = np.reshape(np.array([int(x) for xs in lines for x in xs]), (num_rows, num_cols))
    visited = np.zeros(num_rows * num_cols, dtype=bool).reshape((num_rows, num_cols))
    sizes = []
    low_points = []
    for i, row in enumerate(heightmap):
        for j, num in enumerate(row):
            if is_low_point(num, get_adjacent_locations(heightmap, (i, j))):
                low_points += [(i, j)]

    for point in low_points:
        sizes += [get_basin_size(heightmap, point, visited)]

    sorted_sizes = sorted(sizes, reverse=True)
    return sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
