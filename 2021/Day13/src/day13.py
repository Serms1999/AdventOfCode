from IO.IO_module import read_input_lines
import numpy as np

matrix = 0

def parse_dots(dots_list: list) -> list:
    parsed = []
    for d in dots_list:
        aux = d.split(',')
        parsed += [(int(aux[0]), int(aux[1]))]

    return parsed


def parse_folds(folds_list: list) -> list:
    parsed = []
    i = len('fold along ')
    for f in folds_list:
        aux = f[i:].split('=')
        parsed += [(aux[0], int(aux[1]))]

    return parsed


def find_max_axis(dots_list: list) -> tuple:
    max_x = -1
    max_y = -1

    for t in dots_list:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    return max_x, max_y


def set_dots(dots_list: list) -> None:
    global matrix
    for x, y in dots_list:
        matrix[y, x] = True


def fold_matrix(num: int, vertical: bool) -> None:
    global matrix

    if vertical:
        matrix = np.transpose(matrix)

    m1 = matrix[:num]
    m2 = matrix[num + 1:]

    diff = np.array(np.shape(m1)) - np.array(np.shape(m2))
    if diff[0] < 0:
        aux = np.full((-diff[0], np.shape(m1)[1]), False, dtype=bool)
        m1 = np.vstack((m1, aux))
    elif diff[0] > 0:
        aux = np.full((diff[0], np.shape(m1)[1]), False, dtype=bool)
        m2 = np.vstack((m2, aux))

    matrix = m1 + np.flip(m2, axis=0)

    if vertical:
        matrix = np.transpose(matrix)


def part1(input_lines: list) -> int:
    global matrix
    input_sep = input_lines.index('')
    dots_list = parse_dots(input_lines[0:input_sep])
    folds_list = parse_folds(input_lines[input_sep + 1:])
    max_x, max_y = find_max_axis(dots_list)
    matrix = np.full((max_y + 1, max_x + 1), False, dtype=bool)

    set_dots(dots_list)

    axe, num = folds_list[0]
    fold_matrix(num, axe == 'x')

    return np.count_nonzero(matrix == True)


def part2(input_lines: list) -> None:
    global matrix
    input_sep = input_lines.index('')
    dots_list = parse_dots(input_lines[0:input_sep])
    folds_list = parse_folds(input_lines[input_sep + 1:])
    max_x, max_y = find_max_axis(dots_list)
    matrix = np.full((max_y + 1, max_x + 1), False, dtype=bool)

    set_dots(dots_list)

    for axe, num in folds_list:
        fold_matrix(num, axe == 'x')

    for row in matrix:
        for elem in row:
            print(f'{"#" if elem else "."} ', end='')
        print()


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: ')
    part2(input_lines)


if __name__ == '__main__':
    main()
