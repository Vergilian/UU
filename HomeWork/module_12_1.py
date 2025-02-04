from HumanMoveTest.runner import Runner

import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Vasya')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    def test_run(self):
        runner = Runner('Vasya')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Vasya')
        runner2 = Runner('Yura')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()