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


def plot_school(objects: dict[tuple[int, int], str], limits: tuple[int, int]) -> None:
    for x in range(limits[0]):
        for y in range(limits[1]):
            print(objects.get((x, y), '.'), end='')
        print()


submarine: tuple[int, int] = (0, 0)


def can_move(object_to_move: tuple[int, int], direction: str, objects: dict[tuple[int, int], str]) -> bool:
    direction_vector: dict[str, tuple[int, int]] = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    next_object: tuple[int, int] = (
        object_to_move[0] + direction_vector[direction][0],
        object_to_move[1] + direction_vector[direction][1]
    )

    if objects.get(next_object, '.') == '#':
        return False

    if objects.get(next_object, '.') in ('[', ']'):
        if direction in ('>', '<'):
            return can_move(next_object, direction, objects)

        next_object_pair: tuple[int, int] = (
            next_object[0],
            next_object[1] + (1 if objects.get(next_object, '.') == '[' else -1)
        )
        return can_move(next_object, direction, objects) and can_move(next_object_pair, direction, objects)


    if objects.get(next_object, '.') == 'O' and can_move(next_object, direction, objects):
        return True

    if objects.get(next_object, '.') == '.':
        return True


def move_object(object_to_move: tuple[int, int], direction: str, objects: dict[tuple[int, int], str]) -> None:
    global submarine
    direction_vector: dict[str, tuple[int, int]] = {
        '>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    next_object: tuple[int, int] = (
        object_to_move[0] + direction_vector[direction][0],
        object_to_move[1] + direction_vector[direction][1]
    )

    if objects.get(next_object, '.') == '#':
        return

    if objects.get(next_object, '.') in ('[', ']'):
        if direction in ('>', '<'):
            move_object(next_object, direction, objects)
            objects[next_object] = objects[object_to_move]
            objects[object_to_move] = '.'
        else:
            next_object_pair: tuple[int, int] = (
                next_object[0],
                next_object[1] + (1 if objects.get(next_object, '.') == '[' else -1)
            )
            move_object(next_object, direction, objects)
            move_object(next_object_pair, direction, objects)
            objects[next_object] = objects[object_to_move]
            objects[object_to_move] = '.'
        if object_to_move == submarine:
            submarine = next_object

    if objects.get(next_object, '.') == 'O' and can_move(next_object, direction, objects):
        move_object(next_object, direction, objects)
        objects[next_object] = objects[object_to_move]
        objects[object_to_move] = '.'
        if object_to_move == submarine:
            submarine = next_object


    if objects.get(next_object, '.') == '.':
        objects[next_object] = objects[object_to_move]
        objects[object_to_move] = '.'
        if object_to_move == submarine:
            submarine = next_object



def sum_of_gps_coordinates(input_lines: list[str]) -> int:
    global submarine
    index: int = 0
    objects: dict[tuple[int, int], str] = {}
    while input_lines[index] != '':
        for i, obj in enumerate(input_lines[index]):
            objects[(index, i)] = obj
            if obj == '@':
                submarine = (index, i)
        index += 1

    max_x, max_y = index, len(input_lines[0])
    index += 1

    while index < len(input_lines):
        for direction in input_lines[index]:
            if can_move(submarine, direction, objects):
                move_object(submarine, direction, objects)
        index += 1

    gps_sum: int = 0
    for x in range(max_x):
        for y in range(max_y):
            if objects.get((x, y), '.') in ('O', '['):
                gps_sum += 100 * x + y

    return gps_sum



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
