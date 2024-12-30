from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from math import inf
from heapq import heappop, heappush
from collections.abc import Generator


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(find_exit(read_input_lines(file_name='test_input'), byte_count=12, map_size=(6, 6)), 22)

    def test_part2(self):
        self.assertEqual(first_byte_to_block(read_input_lines(file_name='test_input'), byte_count=12, map_size=(6, 6)), '6,1')


def get_neighbors(cell: tuple[int, int]) -> Generator[tuple[int, int]]:
    directions: list[tuple[int, int]] = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for i, j in directions:
        yield cell[0] + i, cell[1] + j


def dijkstra(memory_map: list[list[str]], distances: dict[tuple[int, int], int], previous: dict[tuple[int, int], tuple[int, int]]) -> None:
    def valid_neighbor(neighbor: tuple[int, int]) -> bool:
        return (0 <= neighbor[0] < len(memory_map) and
                0 <= neighbor[1] < len(memory_map[0]) and
                memory_map[neighbor[0]][neighbor[1]] != '#')

    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (len(memory_map) - 1, len(memory_map[0]) - 1)

    queue: list[tuple[int, tuple[int, int]]] = [(0, start)]

    while queue:
        current_distance, current_cell = heappop(queue)
        if current_cell == end:
            return
        for neighbor_cell in get_neighbors(current_cell):
            if not valid_neighbor(neighbor_cell):
                continue
            new_distance = current_distance + 1
            if new_distance < distances.get(neighbor_cell, inf):
                distances[neighbor_cell] = new_distance
                previous[neighbor_cell] = current_cell
                heappush(queue, (new_distance, neighbor_cell))


def find_exit(input_lines: list[str], byte_count: int, map_size: tuple[int, int] = (70, 70)) -> int:
    memory_map: list[list[str]] = [['.' for _ in range(map_size[0] + 1)] for _ in range(map_size[1] + 1)]
    for index in range(byte_count):
        x, y = map(int, input_lines[index].split(','))
        memory_map[y][x] = '#'

    distances: dict[tuple[int, int], int] = {}
    previous: dict[tuple[int, int], tuple[int, int]] = {}
    dijkstra(memory_map, distances, previous)

    return distances[map_size]


def first_byte_to_block(input_lines: list[str], byte_count: int, map_size: tuple[int, int] = (70, 70)) -> str:
    memory_map: list[list[str]] = [['.' for _ in range(map_size[0] + 1)] for _ in range(map_size[1] + 1)]
    distances: dict[tuple[int, int], int] = {}
    previous: dict[tuple[int, int], tuple[int, int]] = {}

    for index in range(byte_count):
        x, y = map(int, input_lines[index].split(','))
        memory_map[y][x] = '#'

    lower_bound: int = byte_count
    upper_bound: int = len(input_lines) - 1

    while lower_bound <= upper_bound:
        middle: int = lower_bound + (upper_bound - lower_bound) // 2
        new_map: list[list[str]] = [line.copy() for line in memory_map]
        for index in range(byte_count, middle):
            x, y = map(int, input_lines[index].split(','))
            new_map[y][x] = '#'

        distances.clear()
        previous.clear()
        dijkstra(new_map, distances, previous)

        if distances.get(map_size, inf) == inf:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1

    return input_lines[upper_bound]


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Steps to exit: {find_exit(input_lines, byte_count=1024)}',
            output_part2=f'First byte to block: {first_byte_to_block(input_lines, byte_count=1024)}'
        )


if __name__ == '__main__':
    main()
