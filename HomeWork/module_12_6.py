from HumanMoveTest.runner import Runner
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Vasya')
            runner.speed = -5
            if runner.speed < 0:
                raise ValueError(f"Скорость не может быть отрицательной, сейчас {runner.speed}")
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f"{self.__class__.__name__} выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            runner = Runner(123)
            if not isinstance(runner.name, str):
                raise TypeError(f"Имя не может быть только числом, передано {type(runner.name).__name__}")
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f"{self.__class__.__name__} выполнен успешно")

        except TypeError :
            logging.warning("Неверный тип данных для обьекта Runner", exc_info=True)

    def test_challenge(self):
        runner1 = Runner('Vasya')
        runner2 = Runner('Yura')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':

    unittest.main()
