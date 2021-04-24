from enum import Enum
from models.constants import A4_PITCH, _12TH_ROOT_OF_2


class Note(Enum):
    C = 0
    CSharp = 1
    D = 2
    DSharp = 3
    E = 4
    F = 5
    FSharp = 6
    G = 7
    GSharp = 8
    A = 9
    ASharp = 10
    B = 11


class Pitch:
    def __init__(self, note: Note, octave: int):
        if octave < 0:
            raise ValueError('Octave cannot be lower than 0')
        self.note = note
        self.octave = octave

    def steps_from(self, other: 'Pitch'):
        return self.note.value - other.note.value + len(Note) * (self.octave - other.octave)

    @property
    def frequency(self) -> float:
        return A4_PITCH * (_12TH_ROOT_OF_2 ** self.steps_from(Pitch(Note.A, 4)))
