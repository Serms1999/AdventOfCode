from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from typing import List
from IO import read_input_lines, format_output
from collections import Counter


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(lists_distances(read_input_lines(file_name='test_input_part1')), 11)

    def test_part2(self):
        self.assertEqual(similarity_score(read_input_lines(file_name='test_input_part2')), 31)

def split_lists(lines: List[str]) -> List[List[int]]:
    lists: List[List[int]] = [[], []]
    for line in lines:
        num1, num2 = map(int, line.split())
        lists[0].append(num1)
        lists[1].append(num2)
    return lists

def lists_distances(lines: List[str]) -> int:
    lists: List[List[int]] = split_lists(lines)
    lists[0].sort()
    lists[1].sort()

    result: int = 0
    for num1, num2 in zip(lists[0], lists[1]):
        result += abs(num1 - num2)

    return result


def similarity_score(lines: List[str]) -> int:
    lists: List[List[int]] = split_lists(lines)
    counts_list1: Counter[int] = Counter(lists[1])

    score: int = 0
    for num in lists[0]:
        if num in counts_list1:
            score += num * counts_list1[num]

    return score

def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Total distance: {lists_distances(input_lines)}',
            output_part2=f'Similarity score: {similarity_score(input_lines)}'
        )



if __name__ == '__main__':
    main()
