from IO import read_input_lines, format_output
from typing import List
from unittest import TestCase, TestResult, TestLoader, TextTestRunner

class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(count_word_occurrences(read_input_lines(file_name='test_input')), 18)

    def test_part2(self):
        self.assertEqual(count_cross_occurrences(read_input_lines(file_name='test_input')), 9)


def count_word_occurrences(lines: List[str]) -> int:
    occurrences: int = 0
    word = 'XMAS'
    reversed_word: str = word[::-1]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j + len(word) - 1 < len(lines[i]):
                # Horizontal case
                window: str = lines[i][j:j + len(word)]
                occurrences += window == word or window == reversed_word

                if i + len(word) - 1 < len(lines):
                    # Principal diagonal case
                    window: str = ''.join([lines[i + k][j + k] for k in range(len(word))])
                    occurrences += window == word or window == reversed_word

            if i + len(word) - 1 < len(lines):
                # Vertical case
                window: str = ''.join([lines[i + k][j] for k in range(len(word))])
                occurrences += window == word or window == reversed_word

                if j - len(word) + 1 >= 0:
                    # Secondary diagonal case
                    window: str = ''.join([lines[i + k][j - k] for k in range(len(word))])
                    occurrences += window == word or window == reversed_word

    return occurrences


def count_cross_occurrences(lines: List[str]) -> int:
    def check_cross(row: int, col: int) -> bool:
        if lines[row][col] != 'A':
            return False

        if not (lines[row - 1][col - 1], lines[row + 1][col + 1]) in [('M', 'S'), ('S', 'M')]:
            return False

        if not (lines[row - 1][col + 1], lines[row + 1][col - 1]) in [('M', 'S'), ('S', 'M')]:
            return False

        return True

    occurrences: int = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            occurrences += check_cross(i, j)

    return occurrences



def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'\'XMAS\' occurrences: {count_word_occurrences(input_lines)}',
            output_part2=f'\'X-MAS\' occurrences: {count_cross_occurrences(input_lines)}'
        )


if __name__ == '__main__':
    main()
