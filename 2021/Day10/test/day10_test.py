import unittest
from Day10.src.day10 import part1, part2
from IO.IO_module import read_input_lines


class Test(unittest.TestCase):
    def test_part1(self):
        input_lines = read_input_lines(root_file=__file__, file_name='test_input')
        self.assertEqual(part1(input_lines), 26397)

    def test_part2(self):
        input_lines = read_input_lines(root_file=__file__, file_name='test_input')
        self.assertEqual(part2(input_lines), 288957)


if __name__ == '__main__':
    unittest.main()
