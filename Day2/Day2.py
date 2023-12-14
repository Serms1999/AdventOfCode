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


def get_set_required_cubes(set: str) -> dict[str, int]:
    required_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for bag in set.strip().replace(', ', ',').split(','):
        num, color = bag.split(' ')
        required_cubes[color] = int(num)

    return required_cubes


def get_games_power(lines: list[str]) -> int:
    total = 0
    for index, line in enumerate(lines, start=1):
        _, sets = line.split(':')
        sets = sets[1:].split(';')

        required_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for set_requirements in [get_set_required_cubes(set) for set in sets]:
            required_cubes['red'] = max(required_cubes['red'], set_requirements['red'])
            required_cubes['green'] = max(required_cubes['green'], set_requirements['green'])
            required_cubes['blue'] = max(required_cubes['blue'], set_requirements['blue'])

        total += required_cubes['red'] * required_cubes['green'] * required_cubes['blue']

    return total


def main():
    input_lines = read_input_lines(file_name='input')
    print(f'Sum of the valid games: {check_games(input_lines)}')
    print(f'Sum of the powers: {get_games_power(input_lines)}')


if __name__ == '__main__':
    main()
