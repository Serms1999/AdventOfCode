from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from typing import List
from IO import read_input_lines, format_output


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(check_safe_levels(read_input_lines(file_name='test_input')), 2)
    def test_part2(self):
        self.assertEqual(check_safe_levels_with_tolerance(read_input_lines(file_name='test_input')), 4)


def check_report_safety(report: List[str]) -> bool:
    num1, num2 = int(report[0]), int(report[1])
    if num1 > num2 and num1 - num2 <= 3:
        # Case 1: num1 is greater than num2
        for i in range(2, len(report)):
            current_num: int = int(report[i])
            if current_num >= num2 or num2 - current_num > 3:
                return False
            num2 = current_num
    elif num1 < num2 and num2 - num1 <= 3:
        # Case 2: num1 is less than num2
        for i in range(2, len(report)):
            current_num: int = int(report[i])
            if current_num <= num2 or current_num - num2 > 3:
                return False
            num2 = current_num

    else:
        return False

    return True


def check_safe_levels(lines: List[str]) -> int:
    safe_levels: int = 0

    for line in lines:
        safe_levels += check_report_safety(line.split())

    return safe_levels


def check_safe_levels_with_tolerance(lines: List[str]) -> int:
    safe_levels: int = 0

    for line in lines:
        numbers: List[str] = line.split()
        safe: bool = check_report_safety(numbers)
        removed_index: int = 0
        while not safe and removed_index < len(numbers):
            safe = check_report_safety(numbers[:removed_index] + numbers[removed_index + 1:])
            removed_index += 1

        safe_levels += safe

    return safe_levels


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Safe levels: {check_safe_levels(input_lines)}',
            output_part2=f'Safe levels with tolerance: {check_safe_levels_with_tolerance(input_lines)}'
        )



if __name__ == '__main__':
    main()
