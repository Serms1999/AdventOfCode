from IO import read_input_lines


MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def check_set(set: str) -> bool:
    for bag in set.strip().replace(', ', ',').split(','):
        num, color = bag.split(' ')
        num = int(num)

        if num > MAX_CUBES[color]:
            return False

    return True


def check_games(lines: list[str]) -> int:
    total = 0
    for index, line in enumerate(lines, start=1):
        _, sets = line.split(':')
        sets = sets[1:].split(';')
        if all([check_set(set) for set in sets]):
            total += index

    return total


def main():
    input_lines = read_input_lines(file_name='input')
    print(f'Sum of the valid games: {check_games(input_lines)}')


if __name__ == '__main__':
    main()
