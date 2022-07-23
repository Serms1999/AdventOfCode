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
    cnt = [0] * 9

    for s in ages:
        cnt[s] += 1

    for i in range(256):
        new_fish = cnt[0]

        for a in range(0, 8):
            cnt[a] = cnt[a + 1]

        cnt[8] = new_fish
        cnt[6] += new_fish

    return sum(cnt)


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines[0])}')
    print(f'Part two solution: {part2(input_lines[0])}')


if __name__ == '__main__':
    main()