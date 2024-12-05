import unittest
import tests_12_3

RT_ST = unittest.TestSuite()
RT_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RT_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

all_test = unittest.TextTestRunner(verbosity=2)
all_test.run(RT_ST)