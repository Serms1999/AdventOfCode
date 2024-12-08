from IO import read_input_lines, format_output
from typing import List, Tuple, Set, Dict
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(get_antinodes_part1(read_input_lines(file_name='test_input')), 14)

    def test_part2(self):
        self.assertEqual(get_antinodes_part2(read_input_lines(file_name='test_input')), 34)


def generate_antinodes(antenna1: Tuple[int, int], antenna2: Tuple[int, int], distance: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    dx: int = abs(antenna1[0] - antenna2[0])
    dy: int = abs(antenna1[1] - antenna2[1])
    sx: int = 1 if antenna1[0] < antenna2[0] else -1
    sy: int = 1 if antenna1[1] < antenna2[1] else -1

    return (antenna1[0] - distance * sx * dx, antenna1[1] - distance * sy * dy), (antenna2[0] + distance * sx * dx, antenna2[1] + distance * sy * dy)


def check_antinode_inside_bounds(antinode: Tuple[int, int], max_x: int, max_y: int) -> bool:
    return 0 <= antinode[0] < max_y and 0 <= antinode[1] < max_x

def get_antinodes_part1(input_lines: List[str]) -> int:
    antennas: Dict[str, Set[Tuple[int, int]]] = {}
    antinodes: Set[Tuple[int, int]] = set()

    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            if input_lines[i][j] != '.':
                if input_lines[i][j] not in antennas:
                    antennas[input_lines[i][j]] = {(i, j)}
                else:
                    for antenna in antennas[input_lines[i][j]]:
                        antinode1: Tuple[int, int]
                        antinode2: Tuple[int, int]
                        antinode1, antinode2 = generate_antinodes(antenna, (i, j), distance=1)
                        if check_antinode_inside_bounds(antinode1, len(input_lines[0]), len(input_lines)):
                            antinodes.add(antinode1)
                        if check_antinode_inside_bounds(antinode2, len(input_lines[0]), len(input_lines)):
                            antinodes.add(antinode2)
                    antennas[input_lines[i][j]].add((i, j))

    return len(antinodes)


def get_antinodes_part2(input_lines: List[str]) -> int:
    antennas: Dict[str, Set[Tuple[int, int]]] = {}
    antinodes: Set[Tuple[int, int]] = set()

    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            if input_lines[i][j] != '.':
                if input_lines[i][j] not in antennas:
                    antennas[input_lines[i][j]] = {(i, j)}
                    antinodes.add((i, j))
                else:
                    for antenna in antennas[input_lines[i][j]]:
                        for distance in range(max(len(input_lines[i]), len(input_lines))):
                            antinode1: Tuple[int, int]
                            antinode2: Tuple[int, int]
                            antinode1, antinode2 = generate_antinodes(antenna, (i, j), distance=distance)
                            if check_antinode_inside_bounds(antinode1, len(input_lines[0]), len(input_lines)):
                                antinodes.add(antinode1)
                            if check_antinode_inside_bounds(antinode2, len(input_lines[0]), len(input_lines)):
                                antinodes.add(antinode2)

                    antennas[input_lines[i][j]].add((i, j))

    return len(antinodes)


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Antinode unique positions part 1: {get_antinodes_part1(input_lines)}',
            output_part2=f'Antinode unique positions part 2: {get_antinodes_part2(input_lines)}'
        )


if __name__ == '__main__':
    main()
