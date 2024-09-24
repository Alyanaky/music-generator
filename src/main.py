# src/main.py

import tkinter as tk
from tkinter import filedialog, ttk
from .melody_generator import generate_melody
from .chord_generator import generate_chords
from .rhythm_generator import generate_rhythm, play_audio
from .midi_exporter import export_midi

class MusicGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Generator")

        self.load_button = tk.Button(root, text="Load Audio File", command=self.load_audio)
        self.load_button.pack()

        self.generate_melody_button = tk.Button(root, text="Generate Melody", command=self.generate_melody)
        self.generate_melody_button.pack()

        self.generate_chords_button = tk.Button(root, text="Generate Chords", command=self.generate_chords)
        self.generate_chords_button.pack()

        self.generate_rhythm_button = tk.Button(root, text="Генерировать Ритм", command=self.show_rhythm_options)
        self.generate_rhythm_button.pack()

        self.export_button = tk.Button(root, text="Export", command=self.export_music)
        self.export_button.pack()

        self.bpm_label = tk.Label(root, text="BPM:")
        self.bpm_label.pack_forget()  # Скрыть эти элементы по умолчанию
        self.bpm_combobox = ttk.Combobox(root, values=[60, 70, 80, 90, 100, 110, 120])
        self.bpm_combobox.pack_forget()

        self.time_signature_label = tk.Label(root, text="Time Signature (e.g., 4/4):")
        self.time_signature_label.pack_forget()
        self.time_signature_combobox = ttk.Combobox(root, values=["4/4", "3/4", "2/4", "6/8", "5/4", "7/8", "9/8"])
        self.time_signature_combobox.pack_forget()

        self.character_label = tk.Label(root, text="Character (e.g., straight, syncopated):")
        self.character_label.pack_forget()
        self.character_combobox = ttk.Combobox(root, values=["straight", "syncopated", "random", "swing", "shuffle", "triplet", "dotted"])
        self.character_combobox.pack_forget()

        self.last_rhythm = None  # Переменная для хранения последнего ритма

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
        if file_path:
            # Здесь можно добавить логику для загрузки и обработки аудиофайла
            pass

    def generate_melody(self):
        melody = generate_melody(duration=8)  #  Добавьте параметр duration
        play_audio(melody, sr=22050)

    def generate_chords(self):
        chords = generate_chords(duration=8)  #  Добавьте параметр duration
        play_audio(chords, sr=22050)

    def show_rhythm_options(self):
        self.bpm_label.pack()
        self.bpm_combobox.pack()
        self.time_signature_label.pack()
        self.time_signature_combobox.pack()
        self.character_label.pack()
        self.character_combobox.pack()

        # Создайте отдельную кнопку для генерации ритма
        self.generate_rhythm_now_button = tk.Button(root, text="Генерировать", command=self.generate_rhythm)
        self.generate_rhythm_now_button.pack()

    def generate_rhythm(self):
        bpm = int(self.bpm_combobox.get())
        time_signature = self.time_signature_combobox.get()
        character = self.character_combobox.get()
        rhythm = generate_rhythm(bpm, time_signature, character, duration=8)
        play_audio(rhythm, sr=22050)
        self.last_rhythm = rhythm

    def export_music(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mid", filetypes=[("MIDI Files", "*.mid")])
        if file_path:
            # Используйте self.last_rhythm для экспорта финальной музыки
            # (Вам нужно будет реализовать функцию export_midi, которая 
            # принимает массив данных ритма и экспортирует его в MIDI)
            export_midi(file_path, self.last_rhythm)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicGeneratorApp(root)
    root.mainloop()
