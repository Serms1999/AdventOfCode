from IO.IO_module import read_input_lines
import math


def get_adjacent(node: tuple) -> list:
    x, y = node
    return [(x, y - 1), (x - 1, y),
            (x + 1, y), (x, y + 1)]


def part1(input_lines: list) -> int:
    nodes = {}
    for i, row in enumerate(input_lines):
        for j, item in enumerate(row):
            nodes[(i, j)] = int(item)

    max_x, max_y = max(nodes)
    best_set = {}
    open_set = [((0, 0), 0)]

    while open_set:
        min_node = (-1, -1)
        min_cost = math.inf
        for node, cost in open_set:
            if cost < min_cost:
                min_node = node
                min_cost = cost

        open_set.remove((min_node, min_cost))

        if min_node in best_set and min_cost >= best_set[min_node]:
            continue
        else:
            best_set[min_node] = min_cost

        if min_node == (max_x, max_y):
            return min_cost

        for adj in get_adjacent(min_node):
            if adj not in nodes:
                continue
            open_set.append((adj, nodes[adj] + min_cost))

    return 0


def part2(input_lines: list) -> int:
    return 0


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part1(input_lines)}')


if __name__ == '__main__':
    main()
