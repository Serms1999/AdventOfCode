from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from math import inf
from heapq import heappop, heappush
from collections.abc import Generator


class PartialTests(TestCase):
    def test_1_part1(self):
        self.assertEqual(maze_score(read_input_lines(file_name='test_input_1')), 7036)

    def test_2_part1(self):
        self.assertEqual(maze_score(read_input_lines(file_name='test_input_2')), 11048)

    def test_1_part2(self):
        self.assertEqual(maze_path(read_input_lines(file_name='test_input_1')), 45)

    def test_2_part2(self):
        self.assertEqual(maze_path(read_input_lines(file_name='test_input_2')), 64)


def get_neighbors(cell: tuple[int, int], direction: int) -> Generator[tuple[int, tuple[int, int], int]]:
    directions: list[tuple[int, int]] = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    yield 1000, cell, (direction - 1) % len(directions)
    yield 1000, cell, (direction + 1) % len(directions)
    new_x, new_y = cell[0] + directions[direction][0], cell[1] + directions[direction][1]
    yield 1, (new_x, new_y), direction


def dijkstra(input_lines: list[str]) -> tuple[int, set[tuple[int, int]]]:
    distances: dict[tuple[tuple[int, int], int], int | float] = {}
    previous_cells: dict[tuple[tuple[int, int], int], set[tuple[tuple[int, int], int]]] = {}
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)
    for i, line in enumerate(input_lines):
        for j, char in enumerate(line):
            if char == 'S':
                start = (i, j)
            elif char == 'E':
                end = (i, j)

    queue: list[tuple[int, tuple[int, int], int]] = [(0, start, 0)]
    lowest_distance: int | float = inf
    end_cells: set[tuple[tuple[int, int], int]] = set()

    while queue:
        current_distance, current_cell, current_direction = heappop(queue)
        if current_distance > distances.get((current_cell, current_direction), inf):
            continue
        distances[(current_cell, current_direction)] = current_distance
        if current_cell == end:
            if current_distance > lowest_distance:
                continue
            lowest_distance = current_distance
            end_cells.add((current_cell, current_direction))
        for neighbor_distance, neighbor_cell, neighbor_direction in get_neighbors(current_cell, current_direction):
            if input_lines[neighbor_cell[0]][neighbor_cell[1]] == '#':
                continue
            new_distance = current_distance + neighbor_distance
            current_neighbor_distance = distances.get((neighbor_cell, neighbor_direction), inf)
            if new_distance < current_neighbor_distance:
                distances[(neighbor_cell, neighbor_direction)] = new_distance
                previous_cells[(neighbor_cell, neighbor_direction)] = {(current_cell, current_direction)}
                heappush(queue, (new_distance, neighbor_cell, neighbor_direction))
            elif new_distance == current_neighbor_distance:
                previous_cells[(neighbor_cell, neighbor_direction)].add((current_cell, current_direction))

    stack: list[tuple[tuple[int, int], int]] = list(end_cells)
    cells: set[tuple[int, int]] = {end}
    while stack:
        cell = stack.pop(-1)
        for previous_cell in previous_cells.get(cell, []):
            if previous_cell not in cells:
                stack.append(previous_cell)
                cells.add(previous_cell[0])

    return lowest_distance, cells

def maze_score(input_lines: list[str]) -> int:
    return dijkstra(input_lines)[0]


def maze_path(input_lines: list[str]) -> int:
    _, visited_nodes = dijkstra(input_lines)
    return len(visited_nodes)

def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Maze score: {maze_score(input_lines)}',
            output_part2=f'Maze path: {maze_path(input_lines)}'
        )


if __name__ == '__main__':
    main()
