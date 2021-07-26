from midiutil.MidiFile import MIDIFile


def write_wave(midi_file, filename: str = "out.midi"):
    """
    writes midi into a file
    :param midi_file:
    :param filename:
    :return:
    """
    with open(filename, "wb") as midi_file:
        mf.writeFile(midi_file)


# create your MIDI object
mf = MIDIFile(1)  # only 1 track
track = 0  # the only track

time = 0  # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 60  # C4 (middle C)
time = 0  # start on beat 0
duration = 1  # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64  # E4
time = 2  # start on beat 2
duration = 1  # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67  # G4
time = 4  # start on beat 4
duration = 1  # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)