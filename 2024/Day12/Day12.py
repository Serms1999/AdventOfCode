from IO import read_input_lines, format_output
from unittest import TestCase, TestResult, TestLoader, TextTestRunner


class PartialTests(TestCase):
    def test_part1(self):
        self.assertEqual(fence_price_perimeter(read_input_lines(file_name='test_input')), 1930)

    def test_part2(self):
        self.assertEqual(fence_price_sides(read_input_lines(file_name='test_input')), 1206)

MAP_LIMITS: tuple[int, int] = (-1, -1)

class Region:
    def __init__(self, plant_type: str):
        self.plant_type: str = plant_type
        self.plants: set[tuple[int, int]] = set()
        self.plant_sides: dict[tuple[int, int], set[str]] = {}

    def perimeter(self) -> int:
        perimeter: int = 0
        for plant in self.plants:
            perimeter += 4
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                perimeter -= (plant[0] + dx, plant[1] + dy) in self.plants
        return perimeter

    def sides(self) -> int:
        sides: int = 0
        first_row: int = min(self.plants, key=lambda x: x[0])[0]
        last_row: int = max(self.plants, key=lambda x: x[0])[0]
        first_col: int = min(self.plants, key=lambda x: x[1])[1]
        last_col: int = max(self.plants, key=lambda x: x[1])[1]

        for row in range(first_row, last_row + 1):
            last_view_up: bool | None = None
            last_view_down: bool | None = None
            for col in range(first_col, last_col + 1):
                if (value := 'up' in self.plant_sides.get((row, col), set())) != last_view_up:
                    sides += value
                    last_view_up = value

                if (value := 'down' in self.plant_sides.get((row, col), set())) != last_view_down:
                    sides += value
                    last_view_down = value

        for col in range(first_col, last_col + 1):
            last_view_left: bool | None = None
            last_view_right: bool | None = None
            for row in range(first_row, last_row + 1):
                if (value := 'left' in self.plant_sides.get((row, col), set())) != last_view_left:
                    sides += value
                    last_view_left = value

                if (value := 'right' in self.plant_sides.get((row, col), set())) != last_view_right:
                    sides += value
                    last_view_right = value

        return sides


    def impute_sides(self) -> None:
        for plant in self.plants:
            neighbors: dict[str, tuple[int, int]] = {
                'up': (plant[0] - 1, plant[1]),
                'down': (plant[0] + 1, plant[1]),
                'left': (plant[0], plant[1] - 1),
                'right': (plant[0], plant[1] + 1)
            }

            possible_sides: set[str] = set(neighbors.keys())
            for side, neighbor in neighbors.items():
                if neighbor in self.plants:
                    possible_sides.remove(side)

            self.plant_sides[plant] = possible_sides


    def area(self) -> int:
        return len(self.plants)

    def fence_price_perimeter(self) -> int:
        return self.perimeter() * self.area()

    def fence_price_sides(self) -> int:
        return self.sides() * self.area()

    def __str__(self) -> str:
        return f'Plant type: {self.plant_type} Plants: {self.plants}\nPerimeter: {self.perimeter()} Sides: {self.sides()} Area: {self.area()}'

    def __repr__(self) -> str:
        return f'{self.plant_type} {self.plants}'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Region):
            return False
        return self.plant_type == other.plant_type and self.plants == other.plants

    def __hash__(self) -> int:
        return hash((self.plant_type, frozenset(self.plants)))


def get_regions(plant_map: list[str]) -> set[Region]:
    global MAP_LIMITS
    seen: set[tuple[int, int]] = set()
    regions: set[Region] = set()

    MAP_LIMITS = (len(plant_map), len(plant_map[0]))

    def dfs(x: int, y: int, plant_type: str) -> None:
        if (x, y) in seen:
            return

        if plant_map[x][y] != plant_type:
            return

        seen.add((x, y))
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= x + dx < MAP_LIMITS[0] and 0 <= y + dy < MAP_LIMITS[1]:
                dfs(x + dx, y + dy, plant_type)

    for i in range(MAP_LIMITS[0]):
        for j in range(MAP_LIMITS[1]):
            if (i, j) not in seen:
                region: Region = Region(plant_map[i][j])
                dfs(i, j, plant_map[i][j])
                region.plants = seen
                region.impute_sides()
                regions.add(region)
                seen = set()

    return regions


def fence_price_perimeter(input_lines) -> int:
    plant_map: set[Region] = get_regions(input_lines)
    return sum(map(lambda region: region.fence_price_perimeter(), plant_map))


def fence_price_sides(input_lines) -> int:
    plant_map: set[Region] = get_regions(input_lines)
    return sum(map(lambda region: region.fence_price_sides(), plant_map))


def main() -> None:
    result: TestResult = TextTestRunner().run(TestLoader().loadTestsFromTestCase(PartialTests))
    if result.wasSuccessful():
        input_lines: list[str] = read_input_lines(file_name='input')
        format_output(
            output_part1=f'Fence price based on perimeter: {fence_price_perimeter(input_lines)}',
            output_part2=f'Fence price based on sides: {fence_price_sides(input_lines)}'
        )


if __name__ == '__main__':
    main()
