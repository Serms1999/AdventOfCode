from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(process_program(read_input_lines(file_name='test_input_part1')), '4,6,3,5,6,3,5,2,1,0')

    def test_part2(self):
        self.assertEqual(find_initial_value(read_input_lines(file_name='test_input_part2')), 117440)


class Registers:
    def __init__(self) -> None:
        self.registers: dict[str, int] = {'A': 0, 'B': 0, 'C': 0}

    def __getitem__(self, key: int | str) -> int:
        if isinstance(key, str):
            if key not in self.registers:
                return -1

            return self.registers[key]

        if key < 1 or key >= 7:
            return -1

        if 1 <= key <= 3:
            return key

        return self.registers[('A', 'B', 'C')[key - 4]]

    def __setitem__(self, key: int | str, value: int) -> None:
        if isinstance(key, str):
            if key not in self.registers:
                return

            self.registers[key] = value
            return

        if key < 1 or key >= 7:
            return

        if 1 <= key <= 3:
            raise ValueError(f'Cannot set value of register {key}')

        self.registers[('A', 'B', 'C')[key - 4]] = value

    def __repr__(self):
        return f'{self.registers}'

    def __str__(self):
        return f'Registers: {{\n    A: {self.registers["A"]},\n    B: {self.registers["B"]},\n    C: {self.registers["C"]}\n}}'


def simulate_program(registers: Registers, instructions: list[int]) -> list[int]:
    ip: int = 0
    outputs: list[int] = []

    while 0 <= ip < len(instructions) - 1:
        operation: int = instructions[ip]
        operand: int = instructions[ip + 1]

        if operation == 0:
            registers['A'] >>= registers[operand]
        elif operation == 1:
            registers['B'] ^= operand
        elif operation == 2:
            registers['B'] = registers[operand] % 8
        elif operation == 3 and registers['A'] != 0:
            ip = instructions[ip + 1]
            continue
        elif operation == 4:
            registers['B'] ^= registers['C']
        elif operation == 5:
            outputs.append(registers[operand] % 8)
        elif operation == 6:
            registers['B'] = registers['A'] >> registers[operand]
        elif operation == 7:
            registers['C'] = registers['A'] >> registers[operand]

        ip += 2

    return outputs


def reverse_simulate_program(instructions: list[int], outputs: list[int], a_value: int = 0) -> int:
    if not outputs and instructions[0] != 0:
        return a_value

    registers: Registers = Registers()

    for recovered_bits in range(8):
        registers['A'] = a_value << 3 | recovered_bits
        registers['B'] = 0
        registers['C'] = 0
        ip: int = 0
        while 0 <= ip < len(instructions) - 1:
            operation: int = instructions[ip]
            operand: int = instructions[ip + 1]
            if operation == 1:
                registers['B'] ^= operand
            elif operation == 2:
                registers['B'] = registers[operand] % 8
            elif operation == 4:
                registers['B'] ^= registers['C']
            elif operation == 5:
                if not outputs and registers[operand] % 8 == 0:
                    return registers['A']

                if registers[operand] % 8 == outputs[-1]:
                    new_a_value = reverse_simulate_program(instructions, outputs[:-1], registers['A'])
                    if new_a_value is not None:
                        return new_a_value

            elif operation == 6:
                registers['B'] = registers['A'] >> registers[operand]
            elif operation == 7:
                registers['C'] = registers['A'] >> registers[operand]

            ip += 2



def process_program(input_lines: list[str]) -> str:
    registers: Registers = Registers()

    registers['A'] = int(input_lines[0].split(':')[1])
    registers['B'] = int(input_lines[1].split(':')[1])
    registers['C'] = int(input_lines[2].split(':')[1])

    instructions: list[int] = list(map(int, input_lines[4].split(' ')[1].split(',')))
    outputs: list[int] = simulate_program(registers, instructions)

    return ','.join(map(str, outputs))


def find_initial_value(input_lines: list[str]) -> int:
    registers: Registers = Registers()
    instructions: list[int] = list(map(int, input_lines[4].split(' ')[1].split(',')))

    candidate = reverse_simulate_program(instructions, instructions)

    registers['A'] = candidate
    registers['B'] = 0
    registers['C'] = 0
    outputs: list[int] = simulate_program(registers, instructions)
    if outputs == instructions:
        return candidate

    return -1


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Program output: {process_program(input_lines)}',
            output_part2=f'Initial value: {find_initial_value(input_lines)}'
        )


if __name__ == '__main__':
    main()
