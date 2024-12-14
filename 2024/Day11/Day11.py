from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from functools import cache


class PartialTests(TestCase):
    def test_part1(self):
        test_input_lines = read_input_lines(file_name='test_input')[0].split(sep=' ')
        self.assertEqual(get_stones(input_lines=test_input_lines, blinks=25), 55312)


@cache
def simulate_blink(stone_value: int, remaining_blinks: int) -> int:
    if remaining_blinks == 0:
        return 1

    if stone_value == 0:
        return simulate_blink(1, remaining_blinks - 1)

    stone_value_str: str = str(stone_value)
    if len(stone_value_str) & 1 == 0:
        half: int = len(stone_value_str) >> 1
        return (simulate_blink(int(stone_value_str[:half]), remaining_blinks - 1) +
                simulate_blink(int(stone_value_str[half:]), remaining_blinks - 1))

    return simulate_blink(stone_value * 2024, remaining_blinks - 1)


def get_stones(input_lines: list[str], blinks: int) -> int:
    stones_count: int = 0
    for stone in map(int, input_lines):
        stones_count += simulate_blink(stone, blinks)

    return stones_count


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')[0].split(sep=' ')
        format_output(
            output_part1=f'Stones after 25 blinks: {get_stones(input_lines, blinks=25)}',
            output_part2=f'Stones after 75 blinks: {get_stones(input_lines, blinks=75)}'
        )


if __name__ == '__main__':
    main()
