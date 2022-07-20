import IO.IO_module as IO
import numpy as np


def part1(binaries: list) -> int:
    binaries_bits = np.array([np.array([int(bit) for bit in list(b)]) for b in binaries])
    column_bits = np.transpose(binaries_bits)
    middle = column_bits.shape[1] / 2

    column_sums = [sum(c) for c in column_bits]
    gamma_rate = int(''.join(['1' if s > middle else '0' for s in column_sums]), 2)
    epsilon_rate = int(''.join(['0' if s > middle else '1' for s in column_sums]), 2)

    return gamma_rate * epsilon_rate


def part2(binaries: list) -> int:
    binaries_bits = np.array([np.array([int(bit) for bit in list(b)]) for b in binaries])
    binaries_bits_oxigen = binaries_bits.copy()
    binaries_bits_co2 = binaries_bits.copy()

    for i in range(binaries_bits.shape[1]):
        column_bits_oxigen = np.transpose(binaries_bits_oxigen)
        column_bits_co2 = np.transpose(binaries_bits_co2)
        middle_oxigen = column_bits_oxigen.shape[1] / 2
        column_sum_oxigen = sum(column_bits_oxigen[i])
        middle_co2 = column_bits_co2.shape[1] / 2
        column_sum_co2 = sum(column_bits_co2[i])

        bit_oxigen = 1 if column_sum_oxigen >= middle_oxigen else 0
        bit_co2 = 0 if column_sum_co2 >= middle_co2 else 1
        if len(binaries_bits_oxigen) > 1:
            binaries_bits_oxigen = np.array(list(filter(lambda b: b[i] == bit_oxigen, list(binaries_bits_oxigen))))
        if len(binaries_bits_co2) > 1:
            binaries_bits_co2 = np.array(list(filter(lambda b: b[i] == bit_co2, list(binaries_bits_co2))))

    oxigen_rate = int(''.join([str(bit) for bit in binaries_bits_oxigen[0]]), 2)
    co2_rate = int(''.join([str(bit) for bit in binaries_bits_co2[0]]), 2)

    return oxigen_rate * co2_rate


def main():
    input_lines = IO.read_input_lines()
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
