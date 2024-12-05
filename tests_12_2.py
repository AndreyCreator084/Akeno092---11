import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усейн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            names_dict = {i+1: value.name for i, value in enumerate(test_value.values())}
            print(names_dict)

    def test_runners_1_and_3(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        all_results = tournament.start()
        self.all_results[self._testMethodName] = all_results
        self.assertTrue(list(all_results.keys())[-1] == 2 and list(all_results.values())[-1].name == "Ник")

    def test_runners_2_and_3(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        all_results = tournament.start()
        self.all_results[self._testMethodName] = all_results
        self.assertTrue(list(all_results.keys())[-1] == 2 and list(all_results.values())[-1].name == "Ник")

    def test_runners_1_2_and_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = tournament.start()
        self.all_results[self._testMethodName] = all_results
        self.assertTrue(list(all_results.keys())[-1] == 3 and list(all_results.values())[-1].name == "Ник")

