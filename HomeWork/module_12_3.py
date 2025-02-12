import unittest
import module_12_1
import module_12_2
from HomeWork.module_12_1 import RunnerTest
from HomeWork.module_12_2 import TournamentTest

RunnerTest.is_frozen = True
TournamentTest.is_frozen = False

module_12_3 = unittest.TestSuite()
module_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
module_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(module_12_3)
