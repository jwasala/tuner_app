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

    def __str__(self):
        return self.name.replace('Sharp', '#')


class Pitch:
    def __init__(self, note: Note, octave: int):
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
        note = Note((self.note.value + half_steps_distance) % len(Note))
        octave = self.octave + ((self.note.value + half_steps_distance) // len(Note))

        return Pitch(note, octave)

    @property
    def frequency(self) -> float:
        return A4_PITCH * (_12TH_ROOT_OF_2 ** self.half_steps_distance(Pitch(Note.A, 4)))

    @classmethod
    def from_frequency(cls, frequency: float) -> 'Pitch':
        """
        Constructs and returns Pitch object from frequency.

        :return: Estimated pitch for a given frequency.

        :raise: ValueError: if frequency is lower than 0.
        """
        if frequency < 0:
            raise ValueError('Frequency cannot be lower than 0')

        current = Pitch(Note.A, 4)

        if frequency >= A4_PITCH:
            next = Pitch(Note.ASharp, 4)
            while not current.frequency <= frequency < next.frequency:
                current = next
                next = current.shift(1)
        else:
            next = Pitch(Note.GSharp, 4)
            while not next.frequency < frequency <= current.frequency:
                current = next
                next = current.shift(-1)

        if abs(next.frequency - frequency < current.frequency - frequency):
            return next
        else:
            return current

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
