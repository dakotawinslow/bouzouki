import music
import sequencer

bars = ["I", "I", "I", "I", "IV", "IV", "I", "I", "V", "IV", "I", "V"]

key = "A:maj"
key = music.Key(key)
t_sig = (4, 4)

# Start by building a strum pattern

strum = ["^", "-","^", "-","^", "-","^", "-",]

prog = music.Progression(bars, key)

seq = sequencer.AMYSequence(8, 8) # 1-bar sequence, 8th note divisions

chord: music.Chord = None
def build_bar(i): # Build a single bar of music, playing the ith bar of our pattern
    for eigth in range(8):
        if strum[eigth] == ".":
            continue
        elif strum[eigth] == "^":
            

