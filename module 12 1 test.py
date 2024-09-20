import module12_1 as mod
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        h1 = mod.Runner('Tom')
        for walk in range(10):
            h1.walk()
        self.assertEqual(h1.distance,50)

    def test_run(self):
        h2 = mod.Runner('Sam')
        for run in range(10):
            h2.run()
        self.assertEqual(h2.distance, 100)

    def test_challenge(self):
        h3 = mod.Runner('John')
        h4 = mod.Runner('Frank')
        for run in range(10):
            h3.run()
        for walk in range(10):
            h4.walk()
        self.assertNotEqual(h3.distance, h4.distance)

if __name__ == '__main__':
    unittest.main()

