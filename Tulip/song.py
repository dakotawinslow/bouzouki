import music

class Time_Sig():
    def __init__(self, length, beat):
        self.length = length
        self.beat = beat
    
    def __str__(self):
        return f"{self.length}/{self.beat}"
    
class Note_Value():
    def __init__(self, divider:int, duration=1):
        self.divider = divider
        self.duration = duration
        self.ticks = (192 // divider) * duration

class Beat():
    def __init__(self, note: music.Note, value: Note_Value, velocity = 127):
        self.note = note
        self.velocity = velocity
        self.value = value

class Measure():
    def __init__(self):
        self.time_sig : Time_Sig
        self.beats : dict[int : list[music.Note]]

    def __getitem__(self, index): # make this music-notation aware!
        if index in self.beats.keys():
            return self.beats[index]
        else:
            return []
        
    def __setitem__(self, index, item): # make this music-notation aware!
        if type(item) is not Beat:
            raise ValueError(f"Only Beat items can be added to measures. You tried to add a {type(item)}.")
        if not 0 <= index < 192:
            raise IndexError(f"")
        if index in self.beats.keys():
            self.beats[index].append(item)
        else:
            self.beats[index] = [item]
    def add_beat(self, beat)

class Stanza():
    def __init__(self):
        self.key : music.Key = None
        self.time_sig : Time_Sig = None
        self.measures = []
        pass

class Intro(Stanza):
    pass

class Verse(Stanza):
    pass

class Chorus(Stanza):
    pass

class Bridge(Stanza):
    pass

class Outro(Stanza):
    pass

class Song():
    def __init__(self):
        self.stanzas : list[Stanza] = []
        pass