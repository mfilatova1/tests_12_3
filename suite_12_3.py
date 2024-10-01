import unittest
import tests_12_1, tests_12_2

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)
