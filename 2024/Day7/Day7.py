from IO import read_input_lines, format_output
from typing import List, Tuple
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from itertools import product

class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(get_calibrations(read_input_lines(file_name='test_input'), part=1), 3749)

    def test_part2(self):
        self.assertEqual(get_calibrations(read_input_lines(file_name='test_input'), part=2), 11387)


def check_calibration(numbers: List[int], goal_number: int, operations: Tuple[str, ...]) -> bool:
    result: int = numbers[0]
    for index, op in enumerate(operations):
        if op == '+':
            result += numbers[index + 1]
        elif op == '*':
            result *= numbers[index + 1]
        elif op == '||':
            result = int(f'{result}{numbers[index + 1]}')

    return goal_number == result


def get_calibrations(input_lines: List[str], part: int) -> int:
    valid_calibrations: int = 0
    for line in input_lines:
        goal_number: str
        numbers: str
        goal_number, numbers = line.split(': ')
        numbers: List[int] = list(map(int, numbers.split(' ')))

        valid_operations: Tuple[str, ...] = ('+', '*') if part == 1 else ('+', '||', '*')
        goal_number: int = int(goal_number)
        for operations in product(valid_operations, repeat=len(numbers) - 1):
            if check_calibration(numbers.copy(), goal_number, operations):
                valid_calibrations += goal_number
                break

    return valid_calibrations


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Valid calibrations: {get_calibrations(input_lines, part=1)}',
            output_part2=f'Valid calibrations: {get_calibrations(input_lines, part=2)}'
        )


if __name__ == '__main__':
    main()
