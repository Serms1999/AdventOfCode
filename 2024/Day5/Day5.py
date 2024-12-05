from IO import read_input_lines, format_output
from typing import List, Dict, Tuple, Union
from unittest import TestCase, TestResult, TestLoader, TextTestRunner

class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(check_pages(read_input_lines(file_name='test_input_part1')), 143)
    def test_part2(self):
        self.assertEqual(fix_pages(read_input_lines(file_name='test_input_part1')), 123)


def read_rules(lines: List[str]) -> Tuple[Dict[int, List[Tuple[int, int]]], int]:
    rules: Dict[int, List[Tuple[int, int]]] = {}
    line_index: int = 0
    while lines[line_index] != '':
        rule: Tuple[int, int] = tuple(map(int, lines[line_index].split('|')))
        if rule[0] not in rules:
            rules[rule[0]] = []
        rules[rule[0]].append(rule)

        line_index += 1
    line_index += 1

    return rules, line_index

def check_page_ordering(rules: Dict[int, List[Tuple[int, int]]], ordering: List[str]) -> int:
    for index, page in enumerate(ordering):
        page_number: int = int(page)
        for other_page in ordering[index + 1:]:
            pair: Tuple[int, int] = (page_number, int(other_page))
            if pair not in rules.get(pair[0], []):
                return 0

    return int(ordering[len(ordering) // 2])

def check_pages(lines: List[str]) -> int:
    rules, line_index = read_rules(lines)

    result: int = 0
    while line_index < len(lines):
        pages: List[str] = lines[line_index].split(',')
        result += check_page_ordering(rules, pages)
        line_index += 1

    return result


def fix_page_ordering(rules: Dict[int, List[Tuple[int, int]]], ordering: List[str]) -> Union[int, Tuple[int, int]]:
    for index, page in enumerate(ordering):
        page_number: int = int(page)
        for other_page in ordering[index + 1:]:
            pair: Tuple[int, int] = (page_number, int(other_page))
            if pair not in rules.get(pair[0], []):
                return pair

    return int(ordering[len(ordering) // 2])


def fix_pages(lines: List[str]) -> int:
    rules, line_index = read_rules(lines)

    result: int = 0
    while line_index < len(lines):
        pages: List[str] = lines[line_index].split(',')
        need_fix: bool = False
        value: Union[int, Tuple[int, int]] = fix_page_ordering(rules, pages)
        while not isinstance(value, int):
            need_fix = True
            index1 = pages.index(str(value[0]))
            index2 = pages.index(str(value[1]))
            pages[index1], pages[index2] = pages[index2], pages[index1]
            value = fix_page_ordering(rules, pages)
        else:
            if need_fix:
                result += value

        line_index += 1

    return result


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: List[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Middle pages sum: {check_pages(input_lines)}',
            output_part2=f'Middle pages sum: {fix_pages(input_lines)}'
        )


if __name__ == '__main__':
    main()
