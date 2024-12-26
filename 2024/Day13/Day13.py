from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from re import compile as re_compile, Pattern


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(calculate_tokens(read_input_lines(file_name='test_input')), 480)


def calculate_tokens(input_lines: list[str], unit_error: int = 0) -> int:
    button_pattern: Pattern = re_compile(r'Button [AB]: X\+(\d+), Y\+(\d+)')
    prize_pattern: Pattern = re_compile(r'Prize: X=(\d+), Y=(\d+)')

    tokens: int = 0
    for index in range(0, len(input_lines), 4):
        a_x, a_y = map(int, button_pattern.findall(input_lines[index])[0])
        b_x, b_y = map(int, button_pattern.findall(input_lines[index + 1])[0])
        prize_x, prize_y = map(int, prize_pattern.findall(input_lines[index + 2])[0])

        prize_x += unit_error
        prize_y += unit_error

        determinant: int = a_x * b_y - a_y * b_x
        token_x: float = (prize_x * b_y - prize_y * b_x) / determinant
        token_y: float = (a_x * prize_y - a_y * prize_x) / determinant

        if token_x.is_integer() and token_y.is_integer():
            tokens += int(3.0 * token_x + token_y)

    return tokens


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Required tokens: {calculate_tokens(input_lines)}',
            output_part2=f'Required tokens with unit error: {calculate_tokens(input_lines, unit_error=10_000_000_000_000)}'
        )


if __name__ == '__main__':
    main()
