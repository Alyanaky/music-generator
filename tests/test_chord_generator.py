import unittest
from src.chord_generator import generate_chords

class TestChordGenerator(unittest.TestCase):
    def test_generate_chords(self):
        chords = generate_chords()
        self.assertIsNotNone(chords)
        self.assertEqual(len(chords), 22050 * 5)  # Проверка длины аккордов

if __name__ == '__main__':
    unittest.main()