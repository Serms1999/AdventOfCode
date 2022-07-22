import IO.IO_module as IO
import re
from iteration_utilities import duplicates


def check_diagonal(points: tuple) -> bool:
    x1, y1, x2, y2 = points
    return not ((x1 == x2) or (y1 == y2))


def parse_lines(lines: list) -> list:
    tuples = []
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    for line in lines:
        result = pattern.match(line)
        tuples += [(int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)))]

    return tuples


def expand_tuple(points: tuple, diagonal: bool) -> list:
    x1, y1, x2, y2 = points
    if diagonal:
        result = [(x1, y1)]
        while (x1, y1) != (x2, y2):
            x1 += 1 if x1 < x2 else -1
            y1 += 1 if y1 < y2 else -1
            result += [(x1, y1)]
        return result
    else:
        if x1 == x2:
            return [(x1, y) for y in list(range(min(y1, y2), max(y1, y2) + 1))]

        return [(x, y1) for x in list(range(min(x1, x2), max(x1, x2) + 1))]


def part1(lines: list) -> int:
    tuples = parse_lines(lines)
    ver_hor_tuples = list(filter(lambda t: not check_diagonal(t), tuples))
    points = [expand_tuple(t, diagonal=False) for t in ver_hor_tuples]
    flat_points = [x for xs in points for x in xs]
    duplicated_points = list(duplicates(flat_points))

    return len(set(duplicated_points))


def part2(lines: list) -> int:
    tuples = parse_lines(lines)
    points = [expand_tuple(t, diagonal=check_diagonal(t)) for t in tuples]
    flat_points = [x for xs in points for x in xs]
    duplicated_points = list(duplicates(flat_points))

    return len(set(duplicated_points))


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
