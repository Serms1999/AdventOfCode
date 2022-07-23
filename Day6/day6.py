import IO.IO_module as IO
import numpy as np


def part1(input_str: str) -> int:
    ages = np.array(input_str.split(','), dtype=int)
    num_zeros = np.count_nonzero(ages == 0)
    i = 0
    while True:
        ages -= 1
        ages = np.append(ages, [8] * num_zeros)
        for index, value in enumerate(ages):
            if value == -1:
                ages[index] = 6
        num_zeros = np.count_nonzero(ages == 0)

        i += 1
        if i == 80:
            break

    return len(ages)


def part2(input_str: str) -> int:
    ages = np.array(input_str.split(','), dtype=int)

    count_repeated = np.zeros(9, dtype=int)
    for index, value in np.asarray(np.unique(ages, return_counts=True)).T:
        count_repeated[index] = value

    for i in range(256):
        new_fish = count_repeated[0]

        for a in range(0, 8):
            count_repeated[a] = count_repeated[a + 1]

        count_repeated[8] = new_fish
        count_repeated[6] += new_fish

    return sum(count_repeated)


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines[0])}')
    print(f'Part two solution: {part2(input_lines[0])}')


if __name__ == '__main__':
    main()
