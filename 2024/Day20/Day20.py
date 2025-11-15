from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from collections import deque
from collections.abc import Generator
from itertools import permutations
from math import inf


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(count_savings(read_input_lines(file_name='test_input'), max_cheat=2, min_improvement=0), 44)
    def test_part2(self):
        self.assertEqual(count_savings(read_input_lines(file_name='test_input'), max_cheat=20, min_improvement=50), 285)


def get_adjacent_nodes(racetrack: set[tuple[int, int]], node: tuple[int, int], distance: int = 1) -> Generator[tuple[int, int], None, None]:
    for i in range(-distance, distance + 1):
        for j in range(-(distance - abs(i)), distance - abs(i) + 1):
            if (node[0] + i, node[1] + j) not in racetrack: continue
            yield node[0] + i, node[1] + j



def bfs(racetrack: set[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]) -> dict[tuple[int, int], int]:
    queue: deque[tuple[int, int]] = deque()
    queue.append(start)
    distances: dict[tuple[int, int], int] = {start: 0}
    while queue:
        current_node: tuple[int, int] = queue.popleft()
        if current_node == end: break
        for neighbor in get_adjacent_nodes(racetrack, current_node, distance=1):
            if neighbor not in distances:
                distances[neighbor] = distances.get(current_node, 0) + 1
                queue.append(neighbor)

    return distances


def at_least_n_picoseconds(savings: dict[int, int], n: int = 100) -> int:
    return sum(count for saving, count in savings.items() if saving >= n)


def manhattan_distance(node1: tuple[int, int], node2: tuple[int, int]) -> int:
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def get_racetrack(input_lines: list[str]) -> tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)
    nodes: set[tuple[int, int]] = set()
    for row, line in enumerate(input_lines):
        for col, cell in enumerate(line):
            if cell == '#': continue
            nodes.add((row, col))
            if cell == 'S':
                start: tuple[int, int] = (row, col)
            elif cell == 'E':
                end: tuple[int, int] = (row, col)

    return nodes, start, end


def get_savings(racetrack: set[tuple[int, int]], start:tuple[int, int], end: tuple[int, int], max_cheat: int) -> dict[int, int]:
    distances_from_start: dict[tuple[int, int], int] = bfs(racetrack, start=start, end=end)
    distances_from_end: dict[tuple[int, int], int] = bfs(racetrack, start=end, end=start)

    original_distance: int = distances_from_start.get(end, inf)

    savings: dict[int, int] = {}
    for node1 in racetrack:
        for node2 in get_adjacent_nodes(racetrack, node1, distance=max_cheat):
            if (dist := manhattan_distance(node1, node2)) <= max_cheat:
                new_distance: int = distances_from_start[node1] + dist + distances_from_end[node2]
                saving: int = original_distance - new_distance
                if saving > 0:
                    savings[saving] = savings.get(saving, 0) + 1

    return savings


def count_savings(input_lines: list[str], max_cheat: int, min_improvement: int = 100) -> int:
    racetrack: set[tuple[int, int]]
    start: tuple[int, int]
    end: tuple[int, int]
    racetrack, start, end = get_racetrack(input_lines)

    savings: dict[int, int] = get_savings(racetrack, start, end, max_cheat)

    return at_least_n_picoseconds(savings, n=min_improvement)


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Steps to exit: {count_savings(input_lines, max_cheat=2, min_improvement=100)}',
            output_part2=f'Steps to exit: {count_savings(input_lines, max_cheat=20, min_improvement=100)}',
        )



if __name__ == '__main__':
    main()
