import os
import unittest
from main import find_solution


class TestFixtures(unittest.TestCase):
    def test_simple1_example(self):
        with open(os.path.join("fixtures", "simple1.txt")) as fs:
            output = ["Case #1: 1 1 1"]

            self.assertEqual(find_solution(fs.readlines()), output)

    def test_simple2_example(self):
        with open(os.path.join("fixtures", "simple2.txt")) as fs:
            output = ["Case #1: 1 0 0 0 0",
                      "Case #2: IMPOSSIBLE"]

            self.assertEqual(find_solution(fs.readlines()), output)

    def test_simple3_example(self):
        with open(os.path.join("fixtures", "simple3.txt")) as fs:
            output = ["Case #1: 0 0"]

            self.assertEqual(find_solution(fs.readlines()), output)


if __name__ == '__main__':
    unittest.main()
