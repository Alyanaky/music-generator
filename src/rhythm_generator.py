import numpy as np
import pyaudio

def generate_rhythm(bpm, time_signature, character, duration=8):
    beats_per_minute = bpm
    beats_per_measure, note_value = map(int, time_signature.split('/'))
    seconds_per_beat = 60 / beats_per_minute
    seconds_per_measure = beats_per_measure * seconds_per_beat

    # Генерация ритмического паттерна
    if character == 'straight':
        rhythm = np.ones(beats_per_measure)
    elif character == 'syncopated':
        rhythm = np.array([1, 0, 1, 0, 1, 0, 1, 0])[:beats_per_measure]
    else:
        rhythm = np.random.randint(0, 2, beats_per_measure)

    # Преобразование ритма в аудиоданные
    sr = 22050  # Частота дискретизации
    duration = duration  # Длительность ритма в секундах
    rhythm_audio = np.zeros(int(duration * sr))

    # Параметры для атакующего импульса
    attack_duration = 0.02  # Длительность атакующей части в секундах
    decay_duration = 0.1  # Длительность затухающей части в секундах

    for i, beat in enumerate(rhythm):
        if beat == 1:
            start = int(i * seconds_per_beat * sr)
            end = int((i + 1) * seconds_per_beat * sr)

            # Создаем "щелчок" с "хвостом"
            click_signal = np.zeros(end - start)
            click_signal[:int(0.02 * sr)] = 1  #  Короткая атака
            click_signal[int(0.02 * sr):int(0.05 * sr)] = np.linspace(1, 0, int(0.03 * sr)) #  Затухание
            click_signal = click_signal * 0.8  #  Умножение на коэффициент для регулировки громкости 

            # Добавляем щелчок в ритм
            rhythm_audio[start:start + len(click_signal)] = click_signal

    # Нормализация звука:
    max_amplitude = np.max(np.abs(rhythm_audio))
    if max_amplitude > 0:  # Проверяем, что максимальная амплитуда не равна нулю
        rhythm_audio = rhythm_audio / max_amplitude  # Делим на максимальную амплитуду

    return rhythm_audio

def play_audio(audio_data, sr):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sr,
                    output=True)
    stream.write(audio_data.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
