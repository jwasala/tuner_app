from kivy.properties import ObjectProperty, NumericProperty, StringProperty, ListProperty
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

from models.pitch import Pitch, Note
from models.stream import Stream
from models.tunings import TUNINGS
from kivy.app import App
from kivy.uix.widget import Widget


class TunerWindow(Widget):
    stream = Stream()

    pitches = ListProperty([TUNINGS['guitar standard']])
    tune_statuses = ListProperty([0 for _ in TUNINGS['guitar standard']])
    current_tuning = StringProperty('guitar standard')
    freq = NumericProperty(5)
    freq_diff = NumericProperty(0.0)
    freq_diff_regularized = NumericProperty(0.0)
    pitch = ObjectProperty(Pitch(Note.A, 4))
    power = NumericProperty(1.0e-3)

    def update(self, dt):
        self.pitches = [pitch for pitch, tune in self.stream.strings_status]
        self.tune_statuses = [tune for pitch, tune in self.stream.strings_status]
        self.freq = float(self.stream.status.freq)
        self.freq_diff = float(self.stream.status.freq_diff)
        self.freq_diff_regularized = float(self.stream.status.freq_diff_regularized)
        self.pitch = self.stream.status.closest_pitch
        self.power = float(self.stream.status.sample_power)


class TunerApp(App):

    def build(self):
        tw = TunerWindow()
        tw.stream.start()
        Clock.schedule_interval(tw.update, 0.04 / 60.0)

        layout = GridLayout(
            cols=3,
            rows=2,
            width=500,
            height=80,
            spacing=[20, 20],
            center_x=400,
            center_y=100
        )

        def change_tuning(instance):
            tw.current_tuning = instance.text.lower()
            tw.stream.change_strings([(pitch, 0) for pitch in TUNINGS[instance.text.lower()]])

        for tuning in TUNINGS:
            layout.add_widget(Button(
                text=tuning.capitalize(),
                background_normal='',
                background_color=(0.866, 0.015, 0.149),
                font_name='Roboto',
                on_press=change_tuning
            ))

        tw.add_widget(layout)

        return tw


if __name__ == '__main__':
    Config.set('graphics', 'resizable', False)
    TunerApp().run()
