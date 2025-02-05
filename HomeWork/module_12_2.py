from HumanMoveTest.runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    def run_race(self, race_name, *runners):
        t = Tournament(90, *runners)
        result = t.start()
        result = {place: str(runner) for place, runner in result.items()}
        self.__class__.all_result[race_name] = result
        last_runner = result[max(result.keys())]
        self.assertTrue(last_runner == 'Ник', f"Ошибка: {last_runner} не последний")

    def test_race_usain_nick(self):
        self.run_race("Усэйн и Ник", self.runner1, self.runner3)

    def test_race_andrey_nick(self):
        self.run_race("Андрей и Ник", self.runner2, self.runner3)

    def test_race_usain_andrey_nick(self):
        self.run_race("Усэйн, Андрей и Ник", self.runner1, self.runner2, self.runner3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result.values():
            print(result)


if __name__ == '__main__':
    unittest.main()
