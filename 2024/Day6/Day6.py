from IO import read_input_lines, format_output
from typing import List, Set, Tuple, Dict
from unittest import TestCase, TestResult, TestLoader, TextTestRunner

class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(simulate_path(read_input_lines(file_name='test_input')), 41)
    def test_part2(self):
        self.assertEqual(find_loop_positions(read_input_lines(file_name='test_input')), 6)


def find_starting_position(lines: List[str]) -> Tuple[int, int]:
    for index_x, line in enumerate(lines):
        for index_y, char in enumerate(line):
            if char == '^':
                return index_x, index_y
    return -1, -1


def simulate_path(lines: List[str]) -> int:
    start: Tuple[int, int] = find_starting_position(lines)
    if start == (-1, -1):
        return -1

    x, y = start
    dx, dy = -1, 0
    visited: Dict[Tuple[int, int], Set] = {(x, y): set()}

    while 0 <= x + dx < len(lines) and 0 <= y + dy < len(lines[x]):
        if lines[x + dx][y + dy] == '#':
            dx, dy = dy, -dx
        else:
            x += dx
            y += dy
            if (x, y) not in visited:
                visited[(x, y)] = {(dx, dy)}
            else:
                if (dx, dy) in visited[(x, y)]:
                    return -1
                visited[(x, y)].add((dx, dy))

    return len(visited)


def find_loop_positions(lines: List[str]) -> int:
    looping_positions: Set[Tuple[int, int]] = set()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '#' and lines[i][j] != '^':
                new_lines: List[str] = lines.copy()
                new_lines[i] = new_lines[i][:j] + '#' + new_lines[i][j + 1:]
                if simulate_path(new_lines) == -1:
                    looping_positions.add((i, j))

    return len(looping_positions)


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Number of positions: {simulate_path(input_lines)}',
            output_part2=f'Number of looping positions: {find_loop_positions(input_lines)}'
        )


if __name__ == '__main__':
    main()
