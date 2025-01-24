import numpy as np

def generate_chords():
    duration = 5
    sr = 22050
    chords = np.random.randn(duration * sr)
    return chords
