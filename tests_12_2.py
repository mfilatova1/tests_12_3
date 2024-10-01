import unittest
from tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        res1 = tournament.start()
        TournamentTest.all_results.append(res1)
        self.assertTrue(res1[2] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        res2 = tournament2.start()
        TournamentTest.all_results.append(res2)
        self.assertTrue(res2[2] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        res3 = tournament3.start()
        TournamentTest.all_results.append(res3)
        self.assertTrue(res3[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in enumerate(cls.all_results):
            print(f'{key + 1}: {value}')








