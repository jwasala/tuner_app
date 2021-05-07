from models.pitch import Pitch, Note


A4_PITCH = 440

_12TH_ROOT_OF_2 = 1.05946309436

SAMPLING_RATE = 44100

BLOCK_SIZE = 44100

HIGH_FREQUENCY = 700

LOW_FREQUENCY = 80

TUNINGS = {
    'guitar': {
        'standard': {
            Pitch(Note.E, 2),
            Pitch(Note.A, 2),
            Pitch(Note.D, 3),
            Pitch(Note.G, 3),
            Pitch(Note.B, 3),
            Pitch(Note.E, 4)
        },
        'half-step down': {
            Pitch(Note.DSharp, 2),
            Pitch(Note.GSharp, 2),
            Pitch(Note.CSharp, 3),
            Pitch(Note.FSharp, 3),
            Pitch(Note.ASharp, 3),
            Pitch(Note.DSharp, 4)
        }
    }
}