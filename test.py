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

    def test_simple4_example(self):
        with open(os.path.join("fixtures", "simple4.txt")) as fs:
            output = ["Case #1: 0 0 0 0 1"]

            self.assertEqual(find_solution(fs.readlines()), output)

    def test_simple5_example(self):
        with open(os.path.join("fixtures", "simple5.txt")) as fs:
            output = ["Case #1: IMPOSSIBLE"]

            self.assertEqual(find_solution(fs.readlines()), output)

    def test_simple6_example(self):
        with open(os.path.join("fixtures", "simple6.txt")) as fs:
            output = ["Case #1: 1 0 1 0 0"]

            self.assertEqual(find_solution(fs.readlines()), output)

    def test_backtrack(self):
        with open(os.path.join("fixtures", "back_track.txt")) as fs:
            output = ["Case #1: 0 0 1"]

            self.assertEqual(find_solution(fs.readlines()), output)

    def test_large_dataset(self):
        with open(os.path.join("fixtures", "large_dataset.txt")) as fs:
            # todo: write assert for this
            find_solution(fs.readlines())


if __name__ == '__main__':
    unittest.main()
