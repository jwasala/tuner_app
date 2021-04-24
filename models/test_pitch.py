from unittest import TestCase
from pitch import Pitch, Note


class TestPitch(TestCase):
    def test_steps_from(self):
        self.assertEqual(Pitch(Note.C, 5).half_steps_distance(Pitch(Note.A, 4)), 3)
        self.assertEqual(Pitch(Note.DSharp, 3).half_steps_distance(Pitch(Note.DSharp, 1)), 24)
        self.assertEqual(Pitch(Note.G, 4).half_steps_distance(Pitch(Note.A, 3)), 10)

    def test_frequency(self):
        self.assertAlmostEqual(Pitch(Note.A, 4).frequency, 440, places=2)
        self.assertAlmostEqual(Pitch(Note.B, 0).frequency, 30.87, places=2)
        self.assertAlmostEqual(Pitch(Note.D, 4).frequency, 293.66, places=2)
