from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from functools import cache


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(count_possible_designs(read_input_lines(file_name='test_input')), 6)

    def test_part2(self):
        self.assertEqual(count_all_possible_designs(read_input_lines(file_name='test_input')), 16)


@cache
def is_valid_design(available_patterns: frozenset[str], towel: str) -> bool:
    if not towel:
        return True
    for i in range(len(towel) + 1):
        if towel[:i] in available_patterns and is_valid_design(available_patterns, towel[i:]):
            return True
    return False


@cache
def count_number_of_designs(available_patterns: frozenset[str], towel: str) -> int:
    if not towel:
        return 1
    count: int = 0
    for i in range(len(towel) + 1):
        if towel[:i] in available_patterns:
            count += count_number_of_designs(available_patterns, towel[i:])
    return count


def count_possible_designs(input_lines: list[str]) -> int:
    available_patterns: frozenset[str] = frozenset(input_lines[0].split(', '))
    towels: list[str] = input_lines[2:]

    return sum(is_valid_design(available_patterns, towel) for towel in towels)


def count_all_possible_designs(input_lines: list[str]) -> int:
    available_patterns: frozenset[str] = frozenset(input_lines[0].split(', '))
    towels: list[str] = input_lines[2:]

    return sum(count_number_of_designs(available_patterns, towel) for towel in towels)


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Available design: {count_possible_designs(input_lines)}',
            output_part2=f'All possible designs: {count_all_possible_designs(input_lines)}'
        )


if __name__ == '__main__':
    main()
