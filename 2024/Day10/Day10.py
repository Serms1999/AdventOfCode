from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_1_part1(self):
        self.assertEqual(get_trailheads_scores(read_input_lines(file_name='test_input_1_part1'))[0], 2)

    def test_2_part1(self):
        self.assertEqual(get_trailheads_scores(read_input_lines(file_name='test_input_2_part1'))[0], 4)

    def test_3_part1(self):
        self.assertEqual(get_trailheads_scores(read_input_lines(file_name='test_input_3_part1'))[0], 3)

    def test_4_part1(self):
        self.assertEqual(get_trailheads_scores(read_input_lines(file_name='test_input'))[0], 36)

    def test_part2(self):
        self.assertEqual(get_trailheads_scores(read_input_lines(file_name='test_input'))[1], 81)



def parse_input(input_lines: list[str]) -> list[list[int]]:
    topographic_map: list[list[int]] = []
    for line in input_lines:
        topographic_line: list[int] = []
        for char in line:
            if char != '.':
                topographic_line.append(int(char))
            else:
                topographic_line.append(-1)

        topographic_map.append(topographic_line)
    return topographic_map


def get_trailheads_scores(input_lines: list[str]) -> tuple[int, int]:
    def count_hiking_trails(previous: tuple[int, int], current: tuple[int, int]) -> int:
        hiking_trails: int = 0
        backwards_direction: tuple[int, int] = (previous[0] - current[0], previous[1] - current[1])
        if topographic_map[current[0]][current[1]] != topographic_map[previous[0]][previous[1]] + 1:
            return 0

        if topographic_map[current[0]][current[1]] == 9:
            trailhead_scores[(i, j)].add(current)
            return 1

        if backwards_direction != (1, 0) and current[0] + 1 < len(topographic_map):
            hiking_trails += count_hiking_trails(current, (current[0] + 1, current[1]))

        if backwards_direction != (0, 1) and current[1] + 1 < len(topographic_map[0]):
            hiking_trails += count_hiking_trails(current, (current[0], current[1] + 1))

        if backwards_direction != (-1, 0) and current[0] - 1 >= 0:
            hiking_trails += count_hiking_trails(current, (current[0] - 1, current[1]))

        if backwards_direction != (0, -1) and current[1] - 1 >= 0:
            hiking_trails += count_hiking_trails(current, (current[0], current[1] - 1))

        return hiking_trails

    topographic_map: list[list[int]] = parse_input(input_lines)
    total_hiking_trails: int = 0

    trailhead_scores: dict[tuple[int, int], set[tuple[int, int]]] = {}

    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[0])):
            if topographic_map[i][j] == 0:
                trailhead_scores[(i, j)] = set()
                if i + 1 < len(topographic_map):
                    total_hiking_trails += count_hiking_trails((i, j), (i + 1, j))

                if j + 1 < len(topographic_map[0]):
                    total_hiking_trails += count_hiking_trails((i, j), (i, j + 1))

                if i - 1 >= 0:
                    total_hiking_trails += count_hiking_trails((i, j), (i - 1, j))

                if j - 1 >= 0:
                    total_hiking_trails += count_hiking_trails((i, j), (i, j - 1))

    return sum(len(trailhead) for trailhead in trailhead_scores.values()), total_hiking_trails


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        trailheads_score, hiking_trails = get_trailheads_scores(input_lines)
        format_output(
            output_part1=f'Trailheads score: {trailheads_score}',
            output_part2=f'Total hiking trails: {hiking_trails}'
        )


if __name__ == '__main__':
    main()
