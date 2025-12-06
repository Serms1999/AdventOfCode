from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(count_zeros(read_input_lines(file_name='test_input')), 3)
    def test_part2_example1(self):
        self.assertEqual(count_zeros_method_0x434C49434B(read_input_lines(file_name='test_input')), 6)
    def test_part2_example2(self):
        self.assertEqual(count_zeros_method_0x434C49434B(read_input_lines(file_name='test_input2')), 18)

def count_zeros_method_0x434C49434B(input_lines: list[str]) -> int:
    direction_to_sign: dict[str, int] = {'L': -1, 'R': 1}
    count = 0
    dial: int = 50
    for line in input_lines:
        direction, movement = direction_to_sign[line[0]], int(line[1:])
        whole_rotations, equivalent_movement = movement // 100, movement % 100
        whole_rotations -= equivalent_movement == 0
        new_dial = (dial + (direction * equivalent_movement)) % 100
        crossed_zero = False
        if dial != 0:
            if direction > 0 and new_dial < dial:
                crossed_zero = True
            elif direction < 0 and new_dial > dial:
                crossed_zero = True

        landed_zero = (new_dial == 0)
        count += int(crossed_zero or landed_zero) + whole_rotations
        dial = new_dial

    return count


def count_zeros(input_lines: list[str]) -> int:
    direction_to_sign: dict[str, int] = {'L': -1, 'R': 1}
    count = 0
    dial: int = 50
    for line in input_lines:
        dial += direction_to_sign[line[0]] * int(line[1:])
        dial %= 100
        count += dial == 0

    return count


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Password: {count_zeros(input_lines)}',
            output_part2=f'Password: {count_zeros_method_0x434C49434B(input_lines)}'
        )



if __name__ == '__main__':
    main()
