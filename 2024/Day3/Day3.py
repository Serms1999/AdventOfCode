from IO import read_input_lines, format_output
from typing import List
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from re import Pattern, compile, findall


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(sum_multiplications(read_input_lines(file_name='test_input_part1')), 161)

    def test_part2(self):
        self.assertEqual(conditional_sum_multiplications(read_input_lines(file_name='test_input_part2')), 48)


def sum_multiplications(lines: List[str]) -> int:
    pattern: Pattern[str] = compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    numbers: List[str] = pattern.findall(''.join(lines))
    if numbers:
        return sum([int(x) * int(y) for x, y in numbers])

def conditional_sum_multiplications(lines: List[str]) -> int:
    pattern_dirty: Pattern[str] = compile(r'(mul\(\d{1,3},\d{1,3}\))|(don\'t\(\)|do\(\))')
    clean_list: List[str] = [mul if mul else condition for mul, condition in pattern_dirty.findall(''.join(lines))]

    result: int = 0
    conditional_flag: bool = True
    pattern_mul: Pattern[str] = compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    for element in clean_list:
        if element == 'do()':
            conditional_flag = True
        elif element == 'don\'t()':
            conditional_flag = False
        elif conditional_flag:
            x, y = pattern_mul.match(element).groups()
            result += int(x) * int(y)
    return result

def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Sum multiplications: {sum_multiplications(input_lines)}',
            output_part2=f'Conditional sum multiplications: {conditional_sum_multiplications(input_lines)}'
        )


if __name__ == '__main__':
    main()
