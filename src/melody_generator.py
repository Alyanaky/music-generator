import numpy as np

def generate_melody():
    # Пример генерации случайной мелодии
    duration = 5  # Длительность мелодии в секундах
    sr = 22050  # Частота дискретизации
    melody = np.random.randn(duration * sr)
    return melody