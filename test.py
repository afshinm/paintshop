import os
import unittest
from main import solution


class TestFixtures(unittest.TestCase):
    def test_possible_example(self):

        with open(os.path.join("fixtures", "example.txt")) as fs:
            output = ["Case #1: 1 0 0 0 0",
                      "Case #2: IMPOSSIBLE"]

            self.assertEqual(solution(fs.readlines()), output)


if __name__ == '__main__':
    unittest.main()

