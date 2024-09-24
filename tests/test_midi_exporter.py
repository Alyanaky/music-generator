import unittest
import os
from src.midi_exporter import export_midi

class TestMidiExporter(unittest.TestCase):
    def test_export_midi(self):
        file_path = 'data/output/test.mid'
        export_midi(file_path)
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)  # Удаление файла после теста

if __name__ == '__main__':
    unittest.main()