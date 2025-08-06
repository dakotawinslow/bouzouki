import tulip

status = {
    "note_off": 0x80,
    "note_on": 0x90,
    "touch": 0xA0,
    "control": 0xB0,
    "program": 0xC0,
    "cha_touch": 0xD0,
    "pitch": 0xE0,
}


def check_midi_data_vals(n, d1, d2):
    if not 0 <= n < 16:
        raise ValueError(f"MIDI data out of range: n must be in (0, 15), got value:{n}")
    if not 0 <= d1 < 128:
        raise ValueError(
            f"MIDI data out of range: d1 must be in (0, 127), got value:{d1}"
        )
    if not 0 <= d2 < 128:
        raise ValueError(
            f"MIDI data out of range: d2 must be in (0, 127), got value:{d2}"
        )


def note_on(note, vel=127, cha=0):
    check_midi_data_vals(cha, note, vel)
    tulip.midi_out((status["note_on"] + cha, note, vel))


def note_off(note, vel=127, cha=0):
    check_midi_data_vals(cha, note, vel)
    tulip.midi_out((status["note_off"] + cha, note, vel))


def touch(note, press=64, cha=0):
    check_midi_data_vals(cha, note, press)
    tulip.midi_out((status["touch"] + cha, note, press))


def control(ctl_num, data, cha=0):
    check_midi_data_vals(cha, ctl_num, data)
    tulip.midi_out((status["control"] + cha, ctl_num, data))


def program(prog, cha=0):
    check_midi_data_vals(cha, prog, 0)
    tulip.midi_out((status["control"] + cha, prog, 0))


def cha_touch(press, cha=0):
    check_midi_data_vals(cha, press, 0)
    tulip.midi_out((status["cha_touch"] + cha, press, 0))


def pitch(pitch, cha=0):
    if not 0 <= pitch < 16384:
        raise ValueError(
            f"MIDI data out of range: pitch must be within (0, 16384), got value {pitch}"
        )
    LSB = pitch & 0x7F
    MSB = (pitch >> 7) & 0x7F
    tulip.midi_out((status["control"] + cha, LSB, MSB))
