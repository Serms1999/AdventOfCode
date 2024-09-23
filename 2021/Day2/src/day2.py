from IO.IO_module import read_input_lines


def part1(movements: list) -> int:
    position = 0
    depth = 0

    for move in movements:
        s = move.split()
        direction, value = s[0], int(s[1])

        if direction == 'forward':
            position += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value

    return position * depth


def part2(movements: list) -> int:
    aim = 0
    position = 0
    depth = 0

    for move in movements:
        s = move.split()
        direction, value = s[0], int(s[1])

        if direction == 'forward':
            position += value
            depth += value * aim
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value

    return position * depth


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
