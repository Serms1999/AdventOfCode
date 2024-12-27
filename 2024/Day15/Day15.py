from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_1_part1(self):
        self.assertEqual(sum_of_gps_coordinates(read_input_lines(file_name='test_input_1_part1')), 2028)

    def test_2_part1(self):
        self.assertEqual(sum_of_gps_coordinates(read_input_lines(file_name='test_input_2_part1')), 10092)

    def test_1_part2(self):
        self.assertEqual(sum_of_gps_coordinates(transform_input(read_input_lines(file_name='test_input_1_part2'))), 618)

    def test_2_part2(self):
        self.assertEqual(sum_of_gps_coordinates(transform_input(read_input_lines(file_name='test_input_2_part1'))), 9021)


def transform_input(input_lines: list[str]) -> list[str]:
    new_lines: list[str] = []
    for line in input_lines:
        new_lines.append(line.replace('#', '##')
                         .replace('O', '[]')
                         .replace('.', '..')
                         .replace('@', '@.'))

    return new_lines


def direction_to_vector(direction: str) -> tuple[int, int]:
    return {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }[direction]


class Warehouse:
    def __init__(self, warehouse_map: list[str]):
        self.max_x: int = len(warehouse_map)
        self.max_y: int = len(warehouse_map[0])
        self.objects: dict[tuple[int, int], str] = {}
        for i, line in enumerate(warehouse_map):
            for j, obj in enumerate(line):
                if obj == '@':
                    self.submarine = (i, j)
                if obj != '.':
                    self.objects[(i, j)] = obj


    def can_move(self, object_to_move: tuple[int, int], direction: str):
        new_position: tuple[int, int] = (
            object_to_move[0] + direction_to_vector(direction)[0],
            object_to_move[1] + direction_to_vector(direction)[1]
        )
        other_object: str = self.objects.get(new_position, '.')

        if other_object == 'O':
            return self.can_move(new_position, direction)

        if other_object in ('[', ']'):
            if direction in ('>', '<'):
                return self.can_move(new_position, direction)

            new_position_pair: tuple[int, int] = (
                new_position[0],
                new_position[1] + (1 if other_object == '[' else -1)
            )
            return self.can_move(new_position, direction) and self.can_move(new_position_pair, direction)

        return other_object == '.'


    def move_object(self, object_to_move, direction: str) -> None:
        new_position: tuple[int, int] = (
            object_to_move[0] + direction_to_vector(direction)[0],
            object_to_move[1] + direction_to_vector(direction)[1]
        )
        other_object: str = self.objects.get(new_position, '.')

        if other_object == 'O':
            self.move_object(new_position, direction)

        if other_object in ('[', ']'):
            self.move_object(new_position, direction)
            if direction in ('^', 'v'):
                new_position_pair: tuple[int, int] = (
                    new_position[0],
                    new_position[1] + (1 if other_object == '[' else -1)
                )
                self.move_object(new_position_pair, direction)

        self.objects[new_position] = self.objects.get(object_to_move)
        del self.objects[object_to_move]


    def move_submarine(self, direction: str) -> None:
        if self.can_move(self.submarine, direction):
            self.move_object(self.submarine, direction)
            self.submarine = (
                self.submarine[0] + direction_to_vector(direction)[0],
                self.submarine[1] + direction_to_vector(direction)[1]
            )


    def plot_warehouse(self) -> None:
        for x in range(self.max_x):
            for y in range(self.max_y):
                print(self.objects.get((x, y), '.'), end='')
            print()


    def gps_sum(self) -> int:
        gps_sum: int = 0

        for position, item in self.objects.items():
            if item in ('O', '['):
                gps_sum += 100 * position[0] + position[1]

        return gps_sum


def sum_of_gps_coordinates(input_lines: list[str]) -> int:
    index: int = input_lines.index('') + 1
    warehouse: Warehouse = Warehouse(input_lines[:index])

    while index < len(input_lines):
        for direction in input_lines[index]:
            warehouse.move_submarine(direction)
        index += 1

    return warehouse.gps_sum()


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'GPS sum: {sum_of_gps_coordinates(input_lines)}',
            output_part2=f'GPS sum: {sum_of_gps_coordinates(transform_input(input_lines))}'
        )


if __name__ == '__main__':
    main()
