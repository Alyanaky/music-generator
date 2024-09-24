import unittest
from src.rhythm_generator import generate_rhythm

class TestRhythmGenerator(unittest.TestCase):
    def test_generate_rhythm(self):
        rhythm = generate_rhythm()
        self.assertIsNotNone(rhythm)
        self.assertEqual(len(rhythm), 22050 * 5)  # Проверка длины ритма

if __name__ == '__main__':
    unittest.main()