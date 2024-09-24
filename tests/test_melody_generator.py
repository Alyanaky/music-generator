import unittest
from src.melody_generator import generate_melody

class TestMelodyGenerator(unittest.TestCase):
    def test_generate_melody(self):
        melody = generate_melody()
        self.assertIsNotNone(melody)
        self.assertEqual(len(melody), 22050 * 5)  # Проверка длины мелодии

if __name__ == '__main__':
    unittest.main()