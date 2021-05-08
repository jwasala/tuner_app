from models.pitch import Note, Pitch

TUNINGS = {
    'guitar': {
        'standard': [
            Pitch(Note.E, 2),
            Pitch(Note.A, 2),
            Pitch(Note.D, 3),
            Pitch(Note.G, 3),
            Pitch(Note.B, 3),
            Pitch(Note.E, 4)
        ],
        'half-step down': [
            Pitch(Note.DSharp, 2),
            Pitch(Note.GSharp, 2),
            Pitch(Note.CSharp, 3),
            Pitch(Note.FSharp, 3),
            Pitch(Note.ASharp, 3),
            Pitch(Note.DSharp, 4)
        ]
    }
}
