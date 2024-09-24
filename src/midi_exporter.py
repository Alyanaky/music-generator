import pretty_midi

def export_midi(file_path):
    # Пример экспорта музыки в формате MIDI
    midi = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=0)
    note = pretty_midi.Note(
        velocity=100,
        pitch=64,
        start=0,
        end=1
    )
    instrument.notes.append(note)
    midi.instruments.append(instrument)
    midi.write(file_path)