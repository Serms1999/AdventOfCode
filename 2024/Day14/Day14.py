from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner
from re import compile as re_compile, Pattern
from math import prod
from collections import Counter


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(calculate_safety_factor(read_input_lines(file_name='test_input'), bathroom_size=(11, 7)), 12)


class Robot:
    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]):
        self._position: tuple[int, int] = position
        self._velocity: tuple[int, int] = velocity

    def move(self, limits: tuple[int, int], times: int = 1) -> None:
        self._position = (
            (self._position[0] + self._velocity[0] * times) % limits[0],
            (self._position[1] + self._velocity[1] * times) % limits[1]
        )

    def position(self) -> tuple[int, int]:
        return self._position

    def velocity(self) -> tuple[int, int]:
        return self._velocity

    def __repr__(self):
        return f'{{Robot: {self._position} {self._velocity}}}'

    def __str__(self):
        return f'Robot at {self._position} with velocity {self._velocity}'


def get_quadrant(position: tuple[int, int], bathroom_size: tuple[int, int]) -> int:
    middle_x, middle_y = bathroom_size[0] // 2, bathroom_size[1] // 2
    x_quadrant: int = -1 if position[0] == middle_x else position[0] > middle_x
    y_quadrant: int = -1 if position[1] == middle_y else position[1] > middle_y
    if x_quadrant == -1 or y_quadrant == -1:
        return -1
    return 2 * y_quadrant + x_quadrant


def calculate_safety_factor(input_lines: list[str], bathroom_size: tuple[int, int] = (101, 103)) -> int:
    re_robot: Pattern[str] = re_compile(r'^p=(\d+),(\d+)\sv=(-?\d+),(-?\d+)$')
    quadrants: list[int] = [0, 0, 0, 0]
    for line in input_lines:
        x, y, v_x, v_y = map(int, re_robot.match(line).groups())
        robot: Robot = Robot((x, y), (v_x, v_y))
        robot.move(limits=bathroom_size, times=100)
        if (quadrant := get_quadrant(robot.position(), bathroom_size)) != -1:
            quadrants[quadrant] += 1

    return prod(quadrants)


def plot_robots(robots: list[Robot], bathroom_size: tuple[int, int]) -> list[str]:
    bathroom: list[str] = ['.' * bathroom_size[0] for _ in range(bathroom_size[1])]
    for robot in robots:
        x, y = robot.position()
        bathroom[y] = bathroom[y][:x] + '#' + bathroom[y][x + 1:]

    return bathroom


def check_robots_aligned(robots: list[Robot], number_of_robots: int = 10) -> bool:
    if number_of_robots <= 0:
        return False

    def has_consecutive_positions(groups: dict[int, list[int]]) -> bool:
        for positions in groups.values():
            positions.sort()
            count = 1
            for i in range(1, len(positions)):
                if positions[i] == positions[i - 1] + 1:
                    count += 1
                    if count >= number_of_robots:
                        return True
                else:
                    count = 1
        return False

    robot_positions: list[tuple[int, int]] = sorted(map(lambda robot: robot.position(), robots))

    x_groups = {}
    y_groups = {}
    for x, y in robot_positions:
        x_groups.setdefault(x, []).append(y)
        y_groups.setdefault(y, []).append(x)

    return has_consecutive_positions(x_groups) or has_consecutive_positions(y_groups)


def get_seconds_to_easter_egg(input_lines: list[str], bathroom_size: tuple[int, int] = (101, 103)) -> int:
    re_robot: Pattern[str] = re_compile(r'^p=(\d+),(\d+)\sv=(-?\d+),(-?\d+)$')
    robots: list[Robot] = []
    for line in input_lines:
        x, y, v_x, v_y = map(int, re_robot.match(line).groups())
        robots.append(Robot((x, y), (v_x, v_y)))

    seconds: int = 0
    while not check_robots_aligned(robots):
        for robot in robots:
            robot.move(limits=bathroom_size)
        seconds += 1

    with open('easter_egg.txt', 'w') as file:
        file.write('\n'.join(plot_robots(robots, bathroom_size)))
    return seconds


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Safety factor: {calculate_safety_factor(input_lines)}',
            output_part2=f'Seconds to Easter egg: {get_seconds_to_easter_egg(input_lines)}'
        )


if __name__ == '__main__':
    main()
