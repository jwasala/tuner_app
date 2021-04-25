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

    def half_steps_distance(self, other: 'Pitch') -> int:
        """
        :return:
            Difference of half steps between two pitches, starting from the other.
            Positive number means that the other pitch is lower than the initial one.
        """
        return self.note.value - other.note.value + len(Note) * (self.octave - other.octave)

    def shift(self, half_steps_distance: int) -> 'Pitch':
        """
        :return: Pitch that is higher or lower by a given number of half steps from the initial one.
        """
        return None

    @property
    def frequency(self) -> float:
        return A4_PITCH * (_12TH_ROOT_OF_2 ** self.half_steps_distance(Pitch(Note.A, 4)))

    @classmethod
    def from_frequency(cls, frequency: float) -> 'Pitch':
        """
        Constructs and returns Pitch object from frequency.

        :return: Estimated pitch for a given frequency.
        """
        return None

    def __str__(self):
        return f"{self.note}{self.octave}"

    def __lt__(self, other):
        return self.octave < other.octave or (self.octave == other.octave and self.note.value < other.note.value)

    def __le__(self, other):
        return self.octave < other.octave or (self.octave == other.octave and self.note.value <= other.note.value)

    def __gt__(self, other):
        return self.octave > other.octave or (self.octave == other.octave and self.note.value > other.note.value)

    def __ge__(self, other):
        return self.octave > other.octave or (self.octave == other.octave and self.note.value >= other.note.value)

    def __eq__(self, other):
        return self.octave == other.octave and self.note.value == other.note.value

    def __ne__(self, other):
        return self.octave != other.octave or self.note.value != other.note.value
