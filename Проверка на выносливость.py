import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        one = Runner('Test Walk')
        for _ in range(10):
            one.walk()
        self.assertEqual(one.distance, 50)

    def test_run(self):
        one = Runner('Test Run')
        for _ in range(10):
            one.run()
        self.assertEqual(one.distance, 100)

    def test_challenge(self):
        one = Runner('Test Runner 1')
        two = Runner('Test Runner 2')
        for _ in range(10):
            one.run()
            two.walk()
        self.assertNotEqual(one.distance, two.distance)


if __name__ == '__main__':
    unittest.main()