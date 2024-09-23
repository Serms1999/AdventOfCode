import unittest
from Day15.src.day15 import part1, part2
from IO.IO_module import read_input_lines


class Test(unittest.TestCase):
    def test_part1(self):
        input_lines = read_input_lines(root_file=__file__, file_name='test_input_part1')
        self.assertEqual(part1(input_lines), 40)

    def test_part2(self):
        input_lines = read_input_lines(root_file=__file__, file_name='test_input_part2')
        self.assertEqual(part2(input_lines), 315)


if __name__ == '__main__':
    unittest.main()
