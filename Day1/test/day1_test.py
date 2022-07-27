import unittest
import numpy as np
from Day1.src.day1 import part1, part2
from IO.IO_module import read_input_lines


class Test(unittest.TestCase):
    def test_part1(self):
        input_lines = read_input_lines(root_file=__file__, file_name='test_input')
        measurements = np.array([int(n) for n in input_lines])
        self.assertEqual(part1(measurements), 7)

    def test_part2(self):
        input_lines = read_input_lines(root_file=__file__, file_name='test_input')
        measurements = np.array([int(n) for n in input_lines])
        self.assertEqual(part2(measurements), 5)


if __name__ == '__main__':
    unittest.main()
